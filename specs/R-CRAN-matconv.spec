%global packname  matconv
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          2%{?dist}
Summary:          A Code Converter from the Matlab/Octave Language to R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Transferring over a code base from Matlab to R is often a repetitive and
inefficient use of time. This package provides a translator for Matlab /
Octave code into R code. It does some syntax changes, but most of the
heavy lifting is in the function changes since the languages are so
similar. Options for different data structures and the functions that can
be changed are given. The Matlab code should be mostly in adherence to the
standard style guide but some effort has been made to accommodate
different number of spaces and other small syntax issues. This will not
make the code more R friendly and may not even run afterwards. However,
the rudimentary syntax, base function and data structure conversion is
done quickly so that the maintainer can focus on changes to the design
structure.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
