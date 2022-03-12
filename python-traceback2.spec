%global srcname traceback2

Name:		python-%{srcname}
Version:	1.4.0
Release:	2
Summary:	Backports of the traceback module
Group:		Development/Python
License:	Python Software Foundation License
URL:		https://github.com/testing-cabal/traceback2
Source0:	https://pypi.python.org/packages/source/t/%{srcname}/%{srcname}-%version.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(pbr)
Requires:	python3dist(linecache2)

%description
A backport of traceback to older supported Pythons.

%prep
%autosetup -n %{srcname}-%{version}


%build
%py_build

%install
%py_install

%files
%doc AUTHORS ChangeLog README.rst
%{python_sitelib}/%{srcname}
%{python_sitelib}/%{srcname}-%{version}-py%{py_ver}.egg-info
