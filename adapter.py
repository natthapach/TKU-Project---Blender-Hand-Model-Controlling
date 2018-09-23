from transform import Transformer
import bge
import time

class PositionAdapter :
  def __init__(self,
              tip_names=[
                "thumbTip_IK",
                "indexTip_IK",
                "middleTip_IK",
                "ringTip_IK",
                "littleTip_IK",
              ],
              arm_name="arm",
              hand_name="hand") :

    ctrl = bge.logic.getCurrentController()
    self._ob = ctrl.owner
    self._finger_channels = [self._ob.channels[tip] for tip in tip_names]
    self._arm_channels = self._ob.channels[arm_name]
    self._hand_name = hand_name
    self._hand_channel = self._ob.channels[hand_name]
    self._transformer = Transformer()

  def translate(self, matrix) :
    # TODO: query arm lenght instead fix value
    # matrix[5][1] -= 2.41533 # modify arm position with arm lenght
    print("update 0", self._finger_channels[0].location)
    

    # translate arm
    self._transformer.translate(self._arm_channels, self._ob, matrix[-2])

    # rotate hand
    rotation = matrix[-1]
    self._transformer.rotate(self._hand_channel, rotation)

    # update
    self._ob.update()
    print('f1', self._finger_channels[0].location)
    print('f1', self._finger_channels[0].rotation_quaternion)
    # translate finger 
    for i in range(len(matrix) - 2) :
      loc = matrix[i]
      self._transformer.translate(self._finger_channels[i], self._ob, loc)
    
    # update
    self._ob.update()
    print('f2', self._finger_channels[0].location)

      
    