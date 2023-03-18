import bpy

from bpy.types import Operator, Context

from ..common import Registerable


class TWEEN_OT_Reset_Tweens_Op(Operator, Registerable):
    bl_idname = 'tween_follow.reset_tweens'
    bl_label = 'Reset Tweens'
    bl_description = 'Resets all running tweens'

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

        return len(tween_list_items) > 0 and playable and not context.scene.tween_follow_is_playing and not context.scene.tween_reset_done

    def execute(self, context: Context):
        self.report({'INFO'}, "Stopped Running Tweens")

        tween_list_items = context.scene.tween_list_items
        for tween in tween_list_items:
            if tween.tween_target_type == 'Objs':
                for tween_obj in tween.tween_target_list:
                    if tween_obj.tween_target is not None:
                        tween_obj.tween_target.location = tween_obj.tween_pos
            elif tween.tween_target_type == 'Coll':
                for i, tween_obj in enumerate(tween.tween_target_coll.tween_target.all_objects):
                    if tween_obj is not None:
                        tween_obj.location = tween.tween_target_coll.tween_poses[i].tween_pos

        context.scene.tween_reset_done = True

        return {'FINISHED'}
