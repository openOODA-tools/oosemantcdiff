Name:           oosemantcdiff
Version:        0.1.0
Release:        1%{?dist}
Summary:        AI agent semantic delta analyzer detecting behavioral change intent in diffs.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosemantcdiff
Source0:        oosemantcdiff-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosemantcdiff is a sovereign, capability-bounded SEMANTIC DIFF written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosemantcdiff
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosemantcdiff-uninstall

%files
/usr/bin/oosemantcdiff
/usr/bin/oosemantcdiff-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
