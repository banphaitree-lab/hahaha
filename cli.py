import argparse, sys, json
from .bundle import build_channels, build_bundle, bundle_root_from_channels

def main():
    parser = argparse.ArgumentParser(prog="edenwave")
    subparsers = parser.add_subparsers(dest="command")

    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("--xi", type=str, default="1+1j")
    build_parser.add_argument("--vectors", type=str, nargs="*", default=None)
    build_parser.add_argument("-N", type=int, default=40)

    verify_parser = subparsers.add_parser("verify")
    verify_parser.add_argument("--root", type=str, required=True)

    opreturn_parser = subparsers.add_parser("opreturn")
    opreturn_parser.add_argument("--root", type=str, required=True)

    args = parser.parse_args()
    if args.command == "build":
        xi = complex(args.xi)
        vectors = [complex(v) for v in args.vectors] if args.vectors else None
        channels = build_channels(xi=xi, vectors=vectors, N=args.N)
        bundle = build_bundle(channels)
        print(json.dumps(bundle, indent=2))
    elif args.command == "verify":
        root = args.root
        channels = build_channels()
        bundle_root = bundle_root_from_channels(channels)
        print("Valid bundle root" if root == bundle_root else "Invalid bundle root")
    elif args.command == "opreturn":
        root = args.root
        print(f"OP_RETURN: edenwave:{root}")
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()