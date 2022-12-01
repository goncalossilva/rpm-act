BuildRoot:          %{_tmppath}/%{name}-%{version}-build
Name:               act-cli
Version:            0.2.34
Release:            1%{?dist}
Summary:            Run GitHub Actions locally.

License:            MIT
URL:                https://github.com/nektos/act
Source0:            https://github.com/nektos/act/archive/v%{version}.tar.gz

BuildRequires:      golang
BuildRequires:      git
Requires:           (moby or docker or docker-ce or docker-ce-cli or docker-ee)


%description
`act` reads GitHub Actions workflows and determines the set of actions that
need to be run. It uses the Docker API to either pull or build the necessary
images, and determines the execution path based on the defined dependencies.
It then uses the Docker API to run containers for each action based on the
images prepared earlier. The environment variables and filesystem are all
configured to match what GitHub provides.


%prep
tar -xf %{SOURCE0}


%build
cd act-%{version}
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
go build \
    -trimpath \
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -ldflags "-linkmode=external -X main.version=${version}"


%install
rm -rf %{buildroot} && mkdir -p %{buildroot}%{_bindir}/ && cd act-%{version}
install -m 0755 act %{buildroot}%{_bindir}/act
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}/
install -m 0644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/


%verifyscript
%{buildroot}%{_bindir}/act -h


%files
%{_bindir}/act
%license %{_datadir}/licenses/%{name}/LICENSE


%changelog
* Thu Dec 01 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.34
* Tue Nov 01 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.33
* Sat Oct 01 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.32
* Thu Sep 01 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.31
* Mon Aug 01 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.30
* Fri Jul 01 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.29
* Tue Jun 21 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.28
* Tue Jun 21 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.27
* Tue Mar 22 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.26
* Sat Feb 12 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.25
* Sat Feb 12 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.24
* Wed Nov 24 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.25
* Tue Aug 03 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.24
* Fri Jun 11 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.23
* Thu May 06 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.22
* Sun May 02 2021 Gonçalo Silva <goncalossilva@gmail.com>
- act 0.2.21
