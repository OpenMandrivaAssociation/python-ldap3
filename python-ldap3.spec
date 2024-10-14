Name:		python-ldap3
Version:	2.9.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/l/ldap3/ldap3-%{version}.tar.gz
Summary:	A strictly RFC 4510 conforming LDAP V3 pure Python client library
URL:		https://pypi.org/project/ldap3/
License:	LGPL v3
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
A strictly RFC 4510 conforming LDAP V3 pure Python client library

%prep
%autosetup -p1 -n ldap3-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/ldap3
%{py_sitedir}/ldap3-*.*-info
