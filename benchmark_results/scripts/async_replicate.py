import matplotlib.pyplot as plt
import math

# Async replicate parameters
cores = ['1', '4', '8', '16', '32']
exectimes = ['200']
runs = []

for i in range(1, 11):
    runs.append(str(i))

# Graph parameters
font_size = 12
figure_size = [18, 12]
color = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9']
font = {'family' : 'serif', 'serif': ['Palatino'],
        'weight' : 'normal',
        'size'   : 40}
markers = ["o", "^", "*", "P", "s"]

# Initializing x params
error_rate = []
label = ['0.005', '0.01', '0.03', '0.1', '0.25', '0.67']
for i in range(11, 5, -1):
    error_rate.append(i)
    # label.append(str(format((math.exp(-i))*100, '.4f')))

time_async = [2013.540308, 504.441614, 252.517287, 126.45872, 63.8173]
async_counter = 0
# Graph generation
for exectime in exectimes:
    color_counter = 0
    markers_counter = 0
    plt.figure(figsize=(figure_size[0], figure_size[1]))
    plt.rc('font', **font)
    plt.rc('text', usetex=True)

    for core in cores:

        legend_1 = []
        legend_2 = []

        # Initializing async replicate plot values
        time_async_replicate = [0] * 6
        # Initializing async replicate validate plot values
        time_async_replicate_validate = [0] * 6
        # Initializing async repilcate vote
        time_async_replicate_vote = [0] * 6
        # Initializing async replicate vote validate
        time_async_replicate_vote_validate = [0] * 6
        count_replicate = [0] * 6
        count_replicate_vote = [0] * 6
        count_replicate_validate = [0] * 6
        count_replicate_vote_validate = [0] * 6
        for run in runs:
            file = '../benchmarks/async_replicate/async_replicate_' + core + '_' + exectime + '_' + run + '.txt'
            with open(file) as f:
                counter_async = 0
                counter_async_replicate = 0
                counter_async_replicate_validate = 0
                counter_async_replicate_vote = 0
                counter_async_replicate_vote_validate = 0


                counter = 0
                contents = f.read().splitlines()

                i = 1
                while i < len(contents):
                    content = contents[i]

                    if 'Number of asynchronous launches were not enough to get past the injected error levels' in content:
                        i += 4
                    else:
                        line = content.split(' ')
                        if counter % 4 == 0:
                            time_async_replicate[counter_async_replicate] += (float(line[-1]))
                            count_replicate[counter_async_replicate] += 1
                            counter_async_replicate += 1
                        elif counter % 4 == 1:
                            time_async_replicate_validate[counter_async_replicate_validate] += (float(line[-1]))
                            count_replicate_validate[counter_async_replicate_validate] += 1
                            counter_async_replicate_validate += 1
                        elif counter % 4 == 2:
                            time_async_replicate_vote[counter_async_replicate_vote] += (float(line[-1]))
                            count_replicate_vote[counter_async_replicate_vote] += 1
                            counter_async_replicate_vote += 1
                        elif counter % 4 == 3:
                            time_async_replicate_vote_validate[counter_async_replicate_vote_validate] += (float(line[-1]))
                            count_replicate_vote_validate[counter_async_replicate_vote_validate] += 1
                            counter_async_replicate_vote_validate += 1
                        
                        i += 3
                    
                    counter += 1

        # Average times amongst 10 runs
        for i in range(6):
            time_async_replicate[i] = (((time_async_replicate[i]/count_replicate[i]) - (time_async[async_counter]/10.0)))
            time_async_replicate_validate[i] = (((time_async_replicate_validate[i]/count_replicate_validate[i]) - (time_async[async_counter]/10.0)))
            time_async_replicate_vote[i] = (((time_async_replicate_vote[i]/count_replicate_vote[i]) - (time_async[async_counter]/10.0)))
            time_async_replicate_vote_validate[i] = (((time_async_replicate_vote_validate[i]/count_replicate_vote_validate[i]) - (time_async[async_counter]/10.0)))

        async_counter += 1

        p3, = plt.plot(error_rate, time_async_replicate_vote, color[color_counter], linewidth=3.0, marker=markers[markers_counter], markersize=15.0, label=core + ' cores (Async Replicate and variations)')
        color_counter += 1
        markers_counter += 1

    # title = 'Async Replicate: Extra execution time per task vs Probability of error occurrence'
    plt.xticks(error_rate, label[::-1], rotation=45, horizontalalignment='right', fontsize=40)
    plt.yticks(fontsize=40)
    plt.grid()
    plt.ylim(ymin=0)
    plt.legend(bbox_to_anchor=(0.07, 0.82), loc=2, borderaxespad=0.)
    plt.ylabel('Extra execution time per task in us', fontsize=40)
    plt.xlabel('Probability of error occurrence per task (in percentage)', fontsize=40)

    fig_name = 'asyc_replicate_exec_time_' + exectime + '.png'
    plt.savefig('../graphs/async_replicate/' + fig_name, bbox_inches='tight')
    plt.close()