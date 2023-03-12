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
        bpy.app.handlers.frame_change_pre.remove(cls.on_frame_change_pre)

    @classmethod
    def on_frame_change_pre(cls, scene, _):
        if not scene.tween_follow_is_playing:
            return
        for tween in scene.tween_list_items:
            if tween.tween_source is None or not tween.use_tween:
                continue
            src_object = tween.tween_source

            if tween.tween_target_type == 'Objs':
                for target in tween.tween_target_list:
                    tar_object = target.tween_target
                    tar_object.location[2] += (src_object.location[2] -
                                               tar_object.location[2]) * 0.1
