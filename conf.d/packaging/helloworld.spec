###################################
# Léo Hachair, 2022
#
# First spec file written from 
# helloworld-binding.spec
#
###################################


Name: helloworld
Version: 1.0
Release: 0%{?dist}
License: No license 
Summary: helloworld try to be used on redpesk
URL: http://git.ovh.iot/lhachair/my-first-awesome-project.git
Source: %{name}-%{version}.tar.gz

Requires: afb-binder

BuildRequires: afm-rpm-macros
BuildRequires: cmake
BuildRequires: gcc 
BuildRequires: afb-cmake-modules
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(afb-binding)
BuildRequires: pkgconfig(afb-libhelpers)

%description
The helloworld agl service gathers one binding.
- helloworld : says hello

# main package: default install in /var/local/lib/afm/applications/%%{name}
%afm_package
# test package: default install in /var/local/lib/afm/applications/%%{name}-test
%afm_package_test
%afm_package_redtest

%prep
%autosetup -p 1

%build
%afm_configure_cmake
%afm_build_cmake

%install
%afm_makeinstall

%check

%clean

%changelog


* Fri Feb 14 2020 IoT.bzh <redpesk.list.iot.bzh> 8.99.5
- Creation of the spec file from RedPesk generator

