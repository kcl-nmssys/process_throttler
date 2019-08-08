# Process Throttler

This script is designed to be run as a cron job on HPC login nodes and similar, where you wish to restrict long-running CPU/memory-intensive processes - they should be using compute nodes to run these!

For processes using more (on average) than the specified amount of CPU or memory:

1. are reniced to the maximum value (19) after `renice_after` seconds
2. are killed after `kill_after` seconds

Individual users and process paths can be excluded.

## Setup

### CentOS 7

Run `build_centos.sh` to create an rpm package that can be installed using yum.

### Manual installation

Copy the files into their correct locations:

1. `bin/process_throttler` -> `/usr/local/sbin`
2. `etc/cron.d/proccess_throttler` -> `/etc/cron.d` (and edit the path to `process_throttler` in this file)
3. `etc/process_throttler.yaml` -> `/etc`
