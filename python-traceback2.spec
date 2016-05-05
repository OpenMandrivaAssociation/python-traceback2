%global srcname traceback2

Name:           python-%{srcname}
Version:        1.4.0
Release:        1
Summary:        Backports of the traceback module

Group:          Development/Python
License:        Python Software Foundation License
URL:            https://github.com/testing-cabal/traceback2
Source0:        https://pypi.python.org/packages/source/t/%{srcname}/%{srcname}-%version.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3egg(setuptools)

%description
A backport of traceback to older supported Pythons.

%package -n     python2-%{srcname}
Summary:        Backports of the traceback module
Group:          Development/Python
BuildArch:      noarch
BuildRequires:  pkgconfig(python2)
BuildRequires:  pythonegg(setuptools)

%description -n python2-%{srcname}
A backport of traceback to older supported Pythons.

%prep
%setup -q -n %{srcname}-%{version}

cp -a . %{py3dir}

%build
pushd %{py3dir}
%{__python3} setup.py build
popd

%{__python2} setup.py build

%install
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd

%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc AUTHORS ChangeLog README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%files -n python2-%{srcname}
%doc AUTHORS ChangeLog README.rst
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info
