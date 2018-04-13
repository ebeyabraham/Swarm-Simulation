from threading import Thread
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import random

class NavigateMap(Thread):
	def __init__(self,botNum):
		# initiliaze
		Thread.__init__(self)
		self.botNum = botNum
		
	def run(self):
		#bot motion
		rospy.loginfo("bot" + self.botNum + 'started')
		velTopic = '/robot' + self.botNum + '/cmd_vel'
       
		self.cmd_vel = rospy.Publisher(velTopic, Twist, queue_size=10)
     
		r = rospy.Rate(10)

		move_cmd = Twist()
		move_cmd.linear.x = 0.2		#linear velocity along x

		while not rospy.is_shutdown():
			move_cmd.angular.z = random.randint(-2,2)
			self.cmd_vel.publish(move_cmd)
			r.sleep()
                           
	def shutdown(self):
		# stop bot
		rospy.loginfo("Stop Bot")
		self.cmd_vel.publish(Twist())
		rospy.sleep(1)
		
def main():
	try:
		rospy.init_node('Navigate', anonymous=False, disable_signals = True)
		
		bots = []
		
		for botNum in range(3):
			newBot = NavigateMap(str(botNum))
			bots.append(newBot)
		
		for botNum in range(3):
			bots[botNum].start()
		
		for botNum in range(3):
			bots[botNum].join()
		
	except:
		rospy.loginfo("Node terminated.")
		

if __name__ == '__main__':
	main()
