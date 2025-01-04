# main.py
from allArguments import parse_arguments
from logger import app_logger

def main():
    args = parse_arguments()

    app_logger.info(f"Processing data for {args.name} who is {args.age} years old.")
    app_logger.error(f"Processing data for {args.name} who is {args.age} years old.")
    app_logger.warning(f"Processing data for {args.name} who is {args.age} years old.")
    
    print(args.name)

if __name__ == "__main__":
    main()
