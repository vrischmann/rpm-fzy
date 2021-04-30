%global commit 395a2534aca4a704da7501c5e79268420e41d174

Summary:	A simple, fast fuzzy finder for the terminal
Name:		fzy
Version:	1.0
Release:	1%{?dist}

License:	MIT
URL:		https://github.com/jhawthorn/fzy
Source0:	https://github.com/jhawthorn/fzy/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:	make
BuildRequires:	gcc

%description
fzy is a fast, simple fuzzy text selector for the terminal.

%prep
%autosetup -n %{name}-%{commit}

%build
# Makefile doesn't allow overriding from environment, change it
sed -i -e "s:^CFLAGS.*:CFLAGS = %{optflags}:" Makefile
%make_build

%install
make install PREFIX=%{buildroot}%{_prefix}

%files
%{_bindir}/*
%{_mandir}/man1/*

%license LICENSE

%changelog
