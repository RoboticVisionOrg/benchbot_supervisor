import argparse

from .benchbot_supervisor import Supervisor, DEFAULT_PORT

if __name__ == '__main__':
    # Parse all supported arguments
    p = argparse.ArgumentParser(description="Runs the BenchBot Supervisor.")
    p.add_argument('--port',
                   help="Supervisor port number (default: 10000)",
                   default=DEFAULT_PORT)
    p.add_argument('--task-name', help="Name of task")
    p.add_argument(
        '--task-file',
        help="File to load task data (overwritten by other *-file options)")
    p.add_argument('--robot-file', help="File containing robot definition")
    p.add_argument('--actions-file',
                   help="File containing task actions definition")
    p.add_argument('--observations-file',
                   help="File containing task observations definition")
    p.add_argument(
        '--environment-files',
        help=
        "Colon separated list of files containing selected environment metadata"
    )
    args = p.parse_args()

    # Start the supervisor
    s = Supervisor(port=args.port,
                   task_file=args.task_file,
                   task_name=args.task_name,
                   robot_file=args.robot_file,
                   actions_file=args.actions_file,
                   observations_file=args.observations_file,
                   environment_files=args.environment_files)
    s.run()
