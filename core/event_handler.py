import bpy
import math

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
        # fps = bpy.context.scene.render.fps / \
        #     float(bpy.context.scene.render.fps_base)
        for tween in scene.tween_list_items:
            if tween.tween_attractor is None or not tween.use_tween:
                continue
            attr_object = tween.tween_attractor

            objects = []
            tween_objects = []
            tween_params = []
            count = 0
            if tween.tween_target_type == 'Objs':
                objects = [
                    target.tween_target for target in tween.tween_target_list]
                count = len(objects)
                tween_objects = [target for target in tween.tween_target_list]
                tween_params = [target for target in tween.tween_target_list]
            elif tween.tween_target_type == 'Coll':
                objects = [
                    target for target in tween.tween_target_coll.tween_target.all_objects]
                count = len(objects)
                tween_objects = [
                    target for target in tween.tween_target_coll.tween_obj_datas]
                tween_params = [tween.tween_target_coll for _ in range(count)]

            relative_offsets = [[0.0, 0.0, 0.0] for _ in range(count)]
            if tween.keep_offset:
                # Calculate centroid
                centroid = [0.0, 0.0, 0.0]
                for to in tween_objects:
                    for axis in range(3):
                        centroid[axis] += to.tween_pos[axis]
                for axis in range(3):
                    centroid[axis] /= count
                # Calculate relative offset
                for i in range(count):
                    for axis in range(3):
                        relative_offsets[i][axis] = tween_objects[i].tween_pos[axis] - \
                            centroid[axis]

            # Move objects to attractor
            for i in range(count):
                relative_offset = relative_offsets[i]
                tar_object = objects[i]
                # tween_object = tween_objects[i]
                tween_param = tween_params[i]

                target_loc = [(attr_object.location[axis] +
                               relative_offset[axis]) for axis in range(3)]

                # Apply speed on location
                for axis in range(3):
                    tar_object.location[axis] += (
                        target_loc[axis] - tar_object.location[axis]) * tween_param.step_per_frame

        scene.tween_reset_done = False
