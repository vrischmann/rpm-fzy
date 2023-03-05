%global commit 9aa19d3250070f0cc9f5601b805ee6ce3d654377

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
%{__rm} -rf %{buildroot}
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/*
%{_mandir}/man1/*

%license LICENSE

%changelog

* Sun Mar 5 2023 Vincent Rischmann <vincent@rischmann.fr> - 1.0-2
- Update upstream commit

* Sat May 1 2021 Vincent Rischmann <vincent@rischmann.fr> - 1.0-1
- First version
