%global packname  assertive.types
%global packver   0.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          2%{?dist}
Summary:          Assertions to Check Types of Variables

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertive.base >= 0.0.7
BuildRequires:    R-CRAN-assertive.properties 
BuildRequires:    R-codetools 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-assertive.base >= 0.0.7
Requires:         R-CRAN-assertive.properties 
Requires:         R-codetools 
Requires:         R-methods 
Requires:         R-stats 

%description
A set of predicates and assertions for checking the types of variables.
This is mainly for use by other package developers who want to include
run-time testing features in their own packages.  End-users will usually
want to use assertive directly.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
