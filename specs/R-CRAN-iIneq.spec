%global packname  iIneq
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Computing Individual Components of the Gini and the TheilIndices

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach >= 1.4.8
BuildRequires:    R-CRAN-doParallel >= 1.0.15
BuildRequires:    R-parallel 
Requires:         R-CRAN-foreach >= 1.4.8
Requires:         R-CRAN-doParallel >= 1.0.15
Requires:         R-parallel 

%description
Computes individual contributions to the overall Gini and Theil's T and
Theil's L measures and their decompositions by groups such as race,
gender, national origin, with the three functions of iGini(), iTheiT(),
and iTheilL(). For details, see Tim F. Liao (2020)
<doi.org/10.1177/0049124119875961>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/INDEX
