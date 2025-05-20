%define upstream_version 22.10.0
Name:           python3-incremental
Version:        %{upstream_version}
Release:        0
Summary:        Incremental is a small library that versions your Python projects
License:        MIT
URL:            https://github.com/sailfishos/python-incremental
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream
# Remove bundled egg-info
rm -rf incremental.egg-info

%build
%py3_build

%install
%py3_install

# Remove some extra files
rm -f %{python3_sitelib}/incremental-%{upstream_version}-py%{python3_version}.egg-info/not-zip-safe
rm -f %{python3_sitelib}/incremental-%{upstream_version}-py%{python3_version}.egg-info/dependency_links.txt

%files
%license LICENSE
%{python3_sitelib}/incremental
%{python3_sitelib}/incremental-%{upstream_version}-py%{python3_version}.egg-info/
