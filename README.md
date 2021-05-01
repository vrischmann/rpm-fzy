# RPM spec for fzy

## Prerequisites

Setup your tree:
```
$ rpmdev-setuptree
```

## Building

```
$ spectool -C ~/rpmbuild/SOURCES -g fzy.spec
$ rpmbuild -ba fzy.spec
$ sudo dnf install ~/rpmbuild/RPMS/x86_64/fzy-1.0-1.fc34.x86_64.rpm
```
