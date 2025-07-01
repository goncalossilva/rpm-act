BuildRoot:          %{_tmppath}/%{name}-%{version}-build
Name:               act-cli
Version:            0.2.79
Release:            1%{?dist}
Summary:            Run GitHub Actions locally.

License:            MIT
URL:                https://github.com/nektos/act
Source0:            https://github.com/nektos/act/archive/v%{version}.tar.gz

BuildRequires:      golang
BuildRequires:      git
Requires:           (moby or podman or docker or docker-ce or docker-ce-cli or docker-ee)


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
    -ldflags "-linkmode=external -X main.version=%{version}"


%install
rm -rf %{buildroot} && mkdir -p %{buildroot}%{_bindir}/ && cd act-%{version}
install -m 0755 act %{buildroot}%{_bindir}/act
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}/
install -m 0644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/


%verifyscript
%{buildroot}%{_bindir}/act --version


%files
%{_bindir}/act
%license %{_datadir}/licenses/%{name}/LICENSE


%changelog
* Tue Jul 01 2025 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.79
* Sun Jun 01 2025 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.78
* Thu May 01 2025 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.77
* Tue Apr 01 2025 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.76
* Sat Mar 01 2025 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.75
* Mon Feb 10 2025 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.74
* Sat Feb 08 2025 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.73
* Sat Feb 01 2025 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.72
* Wed Jan 01 2025 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.71
* Sun Dec 01 2024 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.70
* Fri Nov 01 2024 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.69
* Tue Oct 01 2024 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.68
* Tue Sep 10 2024 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.67
* Sun Sep 01 2024 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.66
* Thu Aug 01 2024 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.65
* Mon Jul 01 2024 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.64
* Sat Jun 01 2024 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.63
* Wed May 01 2024 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.62
* Mon Apr 01 2024 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.61
* Fri Mar 01 2024 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.60
* Thu Feb 01 2024 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.59
* Thu Feb 01 2024 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.58
* Mon Jan 01 2024 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.57
* Sun Dec 17 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.56
* Fri Dec 01 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.55
* Tue Nov 14 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.54
* Wed Nov 01 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.53
* Sun Oct 01 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.52
* Sat Sep 23 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.51
* Fri Sep 01 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.50
* Tue Aug 01 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.49
* Mon Jul 10 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.48
* Thu Jun 01 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.46
* Mon May 01 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.45
* Sat Apr 01 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.44
* Wed Mar 01 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.43
* Thu Feb 02 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.42
* Wed Feb 01 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.41
* Mon Jan 16 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.40
* Mon Jan 16 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.39
* Mon Jan 16 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.38
* Mon Jan 16 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.36
* Sun Jan 01 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 0.2.35
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
