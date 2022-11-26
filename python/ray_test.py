
import numpy as np
import ray

ray.init(num_cpus=4, ignore_reinit_error=True, dashboard_host="0.0.0.0", dashboard_port=8265, include_dashboard=True)

@ray.remote
def generate_data():
    return np.random.normal(size=1000)

@ray.remote
def aggregate_data(x, y):
    return x + y

if __name__ == '__main__':
    # Generate some random data. This launches 100 tasks that will be scheduled on
    # various nodes. The resulting data will be distributed around the cluster.
    data = [generate_data.remote() for _ in range(100)]

    # Perform a tree reduce.
    while len(data) > 1:
        data.append(aggregate_data.remote(data.pop(0), data.pop(0)))

    # Fetch the result.
    ray.get(data)