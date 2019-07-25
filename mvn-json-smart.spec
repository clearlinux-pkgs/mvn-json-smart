#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-json-smart
Version  : 1.1.1
Release  : 3
URL      : https://repo1.maven.org/maven2/net/minidev/json-smart/1.1.1/json-smart-1.1.1-sources.jar
Source0  : https://repo1.maven.org/maven2/net/minidev/json-smart/1.1.1/json-smart-1.1.1-sources.jar
Source1  : https://repo1.maven.org/maven2/net/minidev/json-smart/1.1.1/json-smart-1.1.1.jar
Source2  : https://repo1.maven.org/maven2/net/minidev/json-smart/1.1.1/json-smart-1.1.1.pom
Source3  : https://repo1.maven.org/maven2/net/minidev/json-smart/1.3.1/json-smart-1.3.1.jar
Source4  : https://repo1.maven.org/maven2/net/minidev/json-smart/1.3.1/json-smart-1.3.1.pom
Source5  : https://repo1.maven.org/maven2/net/minidev/json-smart/2.3/json-smart-2.3.jar
Source6  : https://repo1.maven.org/maven2/net/minidev/json-smart/2.3/json-smart-2.3.pom
Source7  : https://repo1.maven.org/maven2/net/minidev/minidev-parent/2.3/minidev-parent-2.3.pom
Source8  : https://repo1.maven.org/maven2/net/minidev/parent/1.3.1/parent-1.3.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-json-smart-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-json-smart package.
Group: Data

%description data
data components for the mvn-json-smart package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/minidev/json-smart/1.1.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/net/minidev/json-smart/1.1.1/json-smart-1.1.1-sources.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/minidev/json-smart/1.1.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/net/minidev/json-smart/1.1.1/json-smart-1.1.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/minidev/json-smart/1.1.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/net/minidev/json-smart/1.1.1/json-smart-1.1.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/minidev/json-smart/1.3.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/net/minidev/json-smart/1.3.1/json-smart-1.3.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/minidev/json-smart/1.3.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/net/minidev/json-smart/1.3.1/json-smart-1.3.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/minidev/json-smart/2.3
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/net/minidev/json-smart/2.3/json-smart-2.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/minidev/json-smart/2.3
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/net/minidev/json-smart/2.3/json-smart-2.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/minidev/minidev-parent/2.3
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/net/minidev/minidev-parent/2.3/minidev-parent-2.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/minidev/parent/1.3.1
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/net/minidev/parent/1.3.1/parent-1.3.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/net/minidev/json-smart/1.1.1/json-smart-1.1.1-sources.jar
/usr/share/java/.m2/repository/net/minidev/json-smart/1.1.1/json-smart-1.1.1.jar
/usr/share/java/.m2/repository/net/minidev/json-smart/1.1.1/json-smart-1.1.1.pom
/usr/share/java/.m2/repository/net/minidev/json-smart/1.3.1/json-smart-1.3.1.jar
/usr/share/java/.m2/repository/net/minidev/json-smart/1.3.1/json-smart-1.3.1.pom
/usr/share/java/.m2/repository/net/minidev/json-smart/2.3/json-smart-2.3.jar
/usr/share/java/.m2/repository/net/minidev/json-smart/2.3/json-smart-2.3.pom
/usr/share/java/.m2/repository/net/minidev/minidev-parent/2.3/minidev-parent-2.3.pom
/usr/share/java/.m2/repository/net/minidev/parent/1.3.1/parent-1.3.1.pom
