from mathutils import Matrix, Quaternion, Vector

class Transformer :

  def translate(self, channel, armature, location) :
    worldPosition = Vector(location)
    self._set_bone_world_position(channel, armature, worldPosition)
    
  def rotate(self, channel, rotation) :
    channel.joint_rotation = Vector(rotation)
    

  def _get_bone_pose_matrix_cleaned(self, bone):
    offset_m4 = (Matrix.Translation(bone.location) * Quaternion(bone.rotation_quaternion).to_matrix().to_4x4())
    pose_matrix_cleaned = bone.pose_matrix * offset_m4.inverted()
    print(bone.pose_matrix)   # pose matrix not update after translate hand
    return pose_matrix_cleaned
    
  def _set_bone_world_position(self, bone, arm, worldPosition):
    cleaned_matrix = self._get_bone_pose_matrix_cleaned(bone).inverted()
    temp_location = cleaned_matrix * arm.worldTransform.inverted() * worldPosition
    bone.location = temp_location
