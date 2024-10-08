# This config file works only for DTU HPC. Can be changed for local computers or other HPCs.
config = {
    'scheduler': 'slurm',
    'extra_args': ['--mail-type=NONE'],
    'mpiexec': '',
    'nodes': [
            ('xeon56', {'queue': 'slurm',
                        'cores': 56,
                        'memory': '500G'}),
            ('xeon40', {'queue': 'slurm',
                        'cores': 40,
                        'memory': '350G'}),
            ('xeon24', {'queue': 'slurm',
                        'cores': 24,
                        'memory': '250G'}),
            ('xeon16', {'queue': 'slurm',
                        'cores': 16,
                        'memory': '60G'}),
            ('xeon8',  {'queue': 'slurm',
                        'cores': 8,
                        'memory': '22G'}),
            ('xeon24_512', {'queue': 'slurm',
                            'cores': 24,
                            'memory': '500G',}),
            ('xeon24_test', {'queue': 'slurm',
                            'cores': 24,
                            'memory': '500G',}),
            ('xeon40_768', {'queue': 'slurm',
                            'cores': 40,
                            'memory': '750G'}),
            ('sm3090el8', {'queue': 'slurm',
                        'cores': 8,
                        'memory': '191G',
                        'extra_args': ['--gres=gpu:RTX3090:1','--export=ALL,MKL_NUM_THREADS=1,NUMEXPR_NUM_THREADS=1,OMP_NUM_THREADS=1,OPENBLAS_NUM_THREADS=1']}),
            ('sm3090_devel', {'queue': 'slurm',
                        'cores': 8,
                        'memory': '191G',
                        'extra_args': ['--gres=gpu:RTX3090:1','--export=ALL,MKL_NUM_THREADS=1,NUMEXPR_NUM_THREADS=1,OMP_NUM_THREADS=1,OPENBLAS_NUM_THREADS=1']}),            
            ('sm3090', {'queue': 'slurm',
                        'cores': 8,
                        'memory': '191G',
                        'extra_args': ['--gres=gpu:RTX3090:1','--export=ALL,MKL_NUM_THREADS=1,NUMEXPR_NUM_THREADS=1,OMP_NUM_THREADS=1,OPENBLAS_NUM_THREADS=1']}),
            ('sm3090_768', {'queue': 'slurm',
                            'cores': 8,
                            'memory': '768G',
                            'extra_args': ['--gres=gpu:RTX3090:1','--export=ALL,MKL_NUM_THREADS=1,NUMEXPR_NUM_THREADS=1,OMP_NUM_THREADS=1,OPENBLAS_NUM_THREADS=1']})
    ],
    'maximum_diskspace': 4
}
