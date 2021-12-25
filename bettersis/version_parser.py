#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**BETTERSIS.VERSION_PARSER**:
Utilities used to manage version strings.
"""


class Version:
    def __init__(self, major, minor, patch) -> None:
        """
        Represents a version.

        A version is described in this format:
        major.minor.patch

        :param int major: major version
        :param int minor: minor version
        :param int patch: patch version
        """
        self.major = major
        self.minor = minor
        self.patch = patch
    
    def __eq__(self, other):
        """
        Checks if self and other are equals.
        :param Version other: version to check against self
        :return boolean: check result
        """
        if not isinstance(other, Version):
            return False
        
        if self.patch == other.patch and self.minor == other.minor and self.major == other.major:
            return True
        
        return False
        
    def __ne__(self, other):
        """
        Checks if self and other are different.
        :param Version other: version to check against self
        :return boolean: check result
        """
        return not self.__eq__(other)
    
    def __gt__(self, other):
        """
        Checks if self is greater than the other version.
        :param Version other: version to check against self
        :return boolean: check result
        """
        if self.major > other.major:
            return True

        if self.minor > other.minor and self.major == other.major:
            return True
        
        if self.patch > other.patch and self.minor == other.minor and self.major == other.major:
            return True
        
        return False
    
    def __lt__(self, other):
        """
        Checks if self is less than the other version.
        :param Version other: version to check against self
        :return boolean: check result
        """
        if not self.__gt__(other) and not self.__eq__(other):
            return True

        return False
    
    def __le__(self, other):
        """
        Checks if self is less 
        or equal than the other version.
        :param Version other: version to check against self
        :return boolean: check result
        """
        if self.__lt__(other) or self.__eq__(other):
            return True
        return False
    
    def __ge__(self, other):
        """
        Checks if self is greater 
        or equal than the other version.
        :param Version other: version to check against self
        :return boolean: check result
        """
        if self.__gt__(other) or self.__eq__(other):
            return True
        return False
    
    def __repr__(self) -> str:
        """Developer representation of a Version"""
        return "Version({}, {}, {})".format(self.major, self.minor, self.patch)
    
    def __str__(self) -> str:
        """User representation of a Version"""
        return "{}.{}.{}".format(self.major, self.minor, self.patch)


def parse_version(t_version):
    """
    Try to parse the ``<t_version>`` string.
    If the string represents a valid version,
    returns a ``Version()`` object that represents that version.

    :raises ValueError: ``<t_version>`` is not made of digits and 2 dots
    :param str t_version: version string to parse
    :return Version: Version() object that represents the ``<t_version>`` version
    """
    v_version = t_version.split(".")

    if len(v_version) != 3:
        raise ValueError("Couldn't parse version string")
    
    major_version = v_version[0]
    minor_version = v_version[1]
    patch_version = v_version[2]

    try:
        # string must contain integers
        major = int(major_version)
        minor = int(minor_version)
        patch = int(patch_version)
    except ValueError:
        raise ValueError("Version string doesn't contain integers")

    return Version(major, minor, patch)


if __name__ == "__main__":

    versions = []
    for i in range(5, 20):
        for j in range(5, 20):
            for k in range(5, 20):
                versions.append(Version(j, k, i))
    
    import pprint
    print("Versions list:")
    pprint.pprint(versions)

    print("\nordering the list:")
    versions.sort()
    pprint.pprint(versions)

    a = Version(1, 2, 3)
    b = Version(1, 2, 2)
    c = Version(2, 1, 1)
    d = Version(1, 2, 3)

    print("{} < {}: {}".format(a, b, a < b))
    print("{} < {}: {}".format(b, c, b < c))
    print("{} < {}: {}".format(c, a, c < a))

    print("{} > {}: {}".format(a, b, a > b))
    print("{} > {}: {}".format(b, c, b > c))
    print("{} > {}: {}".format(c, a, c > a))

    print("{} != {}: {}".format(c, a, c != a))
    print("{} == {}: {} (different objects)".format(a, d, a == d))
    print("{} == {}: {}".format(a, a, a == a))
