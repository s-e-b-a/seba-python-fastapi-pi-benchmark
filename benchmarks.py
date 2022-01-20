
import time
import platform

# based in https://github.com/alexdedyura/cpu-benchmark
def pi_benchmark(num_samples = 1000, num_repeats = 3):

  start_benchmark = int(num_samples)
  repeat_benchmark = int(num_repeats)
  average_benchmark = 0
  total_benchmark = 0

  for a in range(0,repeat_benchmark):

    start = time.time()

    for i in range(0,start_benchmark):
      for x in range(1,1000):
        3.141592 * 2**x
      for x in range(1,10000):
        float(x) / 3.141592
      for x in range(1,10000):
        float(3.141592) / x

    end = time.time()
    duration = (end - start)
    total_benchmark += duration
    duration = round(duration, 3)
    average_benchmark += duration

  average_benchmark = round(average_benchmark / repeat_benchmark, 3)
  return {"total_execution_time": str(total_benchmark), "average_time": str(average_benchmark), "num_samples": str(num_samples), "num_repeats": str(num_repeats)  }
  