#encoding=utf8

"""
process.py

Donald Disha, RCS ID: dishad
Andrew Aquino, RCS ID: dawneraq
Parker Slote, RCS ID: slotep

This class represents a process being run by a Mnemokinesis memory manager.
"""

class Process(object):
	def __init__(self, pid, memory_frames, arrival_run_times):
		self.pid = pid
		self.memory_frames = int(memory_frames)
		self.arrival_times = [int(time_pair.split('/')[0]) for time_pair in arrival_run_times]
		self.run_times = [int(time_pair.split('/')[1]) for time_pair in arrival_run_times]

		self.times_run = 0
		self.times_to_run = len(self.run_times)

	def __cmp__(self, other):
		"""
		Any “ties” that occur should be handled using the alphabetical order of
		process IDs.
		"""
		return self.pid < other.pid

	def __repr__(self):
		return self.pid