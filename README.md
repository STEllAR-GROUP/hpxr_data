# Artifact Details

This repository contains software and data artifacts required under the SC19 reproducibility appendix.

## Software Artifacts

The benchmarks were run on a single node haswell on Cori.

## Software Artifact Availability

Software artifacts for the paper are present in [benchmark_scripts](benchmark_scripts/). Software artifacts include shell scripts that run a set of binaries for a particular set of times and store the result in a text file.

All the scripts were designed for Cori (i.e. a Slurm environment). To run any of the script do:

```
$ sbatch --qos=regular --time=48:000:00 --nodes=1 --constraint=haswell /path/to/script.sh
```

The above command adds a job requiring 48h of active life on a regular queue of Cori. The job runs on a single haswell node.

**Note:** Each batch of scripts work on relative fix paths to find the binary associated with the script. Make sure to correct the paths before running them.

## Data Artifact Availability

Data artifacts for the paper are present in [benchmarks](benchmark_results/benchmarks/). Hardware artifacts include the results retrieved from running the scripts. Python scripts are provided to generate graphs for the given results.

The files are named in the following manner:

 * benchmark_type + number of cores + benchmark argument (execution time/stencil points) + run number

For example, *async_replay_1_200_1.txt* means that it captures the result coming from async replay benchmarks that were run on a single core at a task grain size of 200us, and that it was the first run of its set.

**Note:** Each batch of scripts work on relative fix paths to find the binary associated with the script. Make sure to correct the paths before running them.