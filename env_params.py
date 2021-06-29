"""
====== Environment controlling ======
## User needs to create a parser for all of params which needed GDR,
## [min, max] represents the UDR-large range.
Take the "Load Balance" env from Park as an example:
"""

import argparse

parser = argparse.ArgumentParser(description='parameters')

# -- Environment --
parser.add_argument('--env', type=str, default='load_balance',
                    help='name of environment (default: load_balance)')

# -- Load Balance --
parser.add_argument('--num_servers', type=int, default=2,
                    help='number of workers (default: 2)')

parser.add_argument('--num_stream_jobs', type=int, default=1000,
                    help='number of streaming jobs (default: 1000)')
parser.add_argument('--num_stream_jobs_min', type=int, default=10,
                    help='minimum number of streaming jobs (default: 10)')
parser.add_argument('--num_stream_jobs_max', type=int, default=100000,
                    help='maximum number of streaming jobs (default: 100000)')

parser.add_argument('--service_rates', type=float, default=[2.0, 4.0], nargs='+',
                    help='workers service rates (default: [2.0, 4.0])')
parser.add_argument('--service_rate_min', type=float, default=0.1,
                    help='minimum service rate (default: 0.1)')
parser.add_argument('--service_rate_max', type=float, default=100,
                    help='maximum service rate (default: 100)')

parser.add_argument('--job_distribution', type=str, default='uniform',
                    help='Job size distribution (default: uniform)')
parser.add_argument('--job_size_min', type=float, default=1.0,
                    help='minimum job size (default: 1.0)')
parser.add_argument('--job_size_max', type=float, default=10000.0,
                    help='maximum job size (default: 10000.0)')

parser.add_argument('--job_interval', type=int, default=100,
                    help='job arrival interval (default: 100)')
parser.add_argument('--job_interval_min', type=int, default=0.1,
                    help='minimum job arrival interval (default: 0.1)')
parser.add_argument('--job_interval_max', type=int, default=1000,
                    help='maximum job arrival interval (default: 1000)')

args = parser.parse_args()
