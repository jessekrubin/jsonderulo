# -*- coding: utf-8 -*-
import os
import re
import sys

from jsonderulo import __version__


def main(env_var="GITHUB_REF") -> int:
    git_ref = os.getenv(env_var, "none")
    tag = re.sub("^refs/tags/v*", "", git_ref.lower())
    version = __version__.lower()
    if tag == version:
        print(
            f"✓ {env_var} env var {git_ref!r} matches package version: {tag!r} == {version!r}"
        )
        return 0
    else:
        print(
            f"✖ {env_var} env var {git_ref!r} does not match package version: {tag!r} != {version!r}"
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
