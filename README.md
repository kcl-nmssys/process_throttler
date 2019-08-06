# Process Throttler

This script is designed to be run as a cron job on HPC login nodes and similar, where you wish to restrict long-running CPU/memory-intensive processes - they should be using compute nodes to run these!

For processes using more (on average) than the specified amount of CPU or memory:

1. are reniced to the maximum value (19) after `renice_after` seconds
2. are killed after `kill_after` seconds

Individual users and process paths can be excluded.

## Setup

The configuration file, `process_throttler.yaml` should be saved to `/etc/`. Place `process_throttler` in `/usr/local/sbin` and create a cron job for the root user:

```
* * * * * /usr/local/sbin/process_throttler
```
