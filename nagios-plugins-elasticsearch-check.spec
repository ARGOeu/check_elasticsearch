Name:		nagios-plugins-elasticsearch-check
Version:	0.5
Release:	1%{?dist}
Summary:	Nagios check_elasticsearch probes
License:	GPLv3+
Packager:	Themis Zamani <themiszamani@gmail.com>

Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}
Requires(pre):  nagios-plugins
AutoReqProv: no

%description
Nagios probes to check functionality of elasticsearch

%prep
%setup -q

%define _unpackaged_files_terminate_build 0 

%install

install -d %{buildroot}/%{_libexecdir}/argo-monitoring/probes/elasticsearch-check
install -d %{buildroot}/%{_sysconfdir}/nagios/plugins/elasticsearch-check
install -m 755 check_elasticsearch %{buildroot}/%{_libexecdir}/argo-monitoring/probes/elasticsearch-check/check_elasticsearch

%files
%dir /%{_libexecdir}/argo-monitoring
%dir /%{_libexecdir}/argo-monitoring/probes/
%dir /%{_libexecdir}/argo-monitoring/probes/elasticsearch-check

%attr(0755,root,root) /%{_libexecdir}/argo-monitoring/probes/elasticsearch-check/check_elasticsearch

%changelog
* Thu Sep 13 2018 Themis Zamani <themiszamani@gmail.com> - 0.1-1
- Initial version of the package. Based on orthecreedence/check_elasticsearch
