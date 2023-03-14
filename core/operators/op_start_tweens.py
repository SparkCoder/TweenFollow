import bpy

from bpy.types import Operator, Context

from ..common import Registerable


class TWEEN_OT_Start_Tweens_Op(Operator, Registerable):
    bl_idname = 'tween_follow.start_tweens'
    bl_label = 'Start Tweens'
    bl_description = 'Starts all active tweens'

    @classmethod
    def register_cls(cls):
        # Register class
        bpy.utils.register_class(cls)

    @classmethod
    def unregister_cls(cls):
        # Unregister class
        bpy.utils.unregister_class(cls)

    @classmethod
    def poll(cls, context: Context):
        tween_list_items = context.scene.tween_list_items

        playable = False
        for tween in tween_list_items:
            if tween.use_tween:
                playable = True
                break

        return len(tween_list_items) > 0 and playable and not context.scene.tween_follow_is_playing

    def execute(self, context: Context):
        self.report({'INFO'}, "Started Active Tweens")

        tween_list_items = context.scene.tween_list_items
        for tween in tween_list_items:
            if tween.tween_target_coll is not None:
                tween.tween_target_coll.tween_pos = tween.tween_target_coll.tween_target.location
            for tween_obj in tween.tween_target_list:
                if tween_obj.tween_target is not None:
                    tween_obj.tween_pos = tween_obj.tween_target.location

        context.scene.tween_follow_is_playing = True

        return {'FINISHED'}
