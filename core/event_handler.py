import bpy

from ..core.common import Registerable


class EventHandler(Registerable):

    @classmethod
    def register_cls(cls):
        # Register events
        bpy.app.handlers.frame_change_pre.append(cls.on_frame_change_pre)

    @classmethod
    def unregister_cls(cls):
        # Unregister events
        if cls.on_frame_change_pre in bpy.app.handlers.frame_change_pre:
            bpy.app.handlers.frame_change_pre.remove(cls.on_frame_change_pre)

    @classmethod
    def on_frame_change_pre(cls, scene, _):
        if not scene.tween_follow_is_playing:
            return
        for tween in scene.tween_list_items:
            if tween.tween_attractor is None or not tween.use_tween:
                continue
            attr_object = tween.tween_attractor

            objects = []
            starts_poses = []
            eases = []
            count = 0
            if tween.tween_target_type == 'Objs':
                objects = [
                    target.tween_target for target in tween.tween_target_list]
                count = len(objects)

                starts_poses = [
                    target.tween_pos for target in tween.tween_target_list]
                eases = [target.ease for target in tween.tween_target_list]
            elif tween.tween_target_type == 'Coll':
                objects = [
                    target for target in tween.tween_target_coll.tween_target.all_objects]
                count = len(objects)

                starts_poses = [
                    target.tween_pos for target in tween.tween_target_coll.tween_poses]
                eases = [tween.tween_target_coll.ease for _ in range(count)]

            relative_offsets = [[0.0, 0.0, 0.0] for _ in range(count)]
            if tween.keep_offset:
                # Calculate centroid
                centroid = [0.0, 0.0, 0.0]
                for pos in starts_poses:
                    for axis in range(3):
                        centroid[axis] += pos[axis]
                for axis in range(3):
                    centroid[axis] /= count
                # Calculate relative offset
                for i in range(count):
                    for axis in range(3):
                        relative_offsets[i][axis] = starts_poses[i][axis] - \
                            centroid[axis]

            # Move objects to attractor
            for i in range(count):
                relative_offset = relative_offsets[i]
                tar_object = objects[i]
                ease = eases[i]
                for axis in range(3):
                    tar_object.location[axis] += ((attr_object.location[axis] +
                                                  relative_offset[axis]) - tar_object.location[axis]) * ease

        scene.tween_reset_done = False
