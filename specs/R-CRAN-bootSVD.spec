%global packname  bootSVD
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          2%{?dist}
Summary:          Fast, Exact Bootstrap Principal Component Analysis for HighDimensional Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ff 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ff 
Requires:         R-parallel 

%description
Implements fast, exact bootstrap Principal Component Analysis and Singular
Value Decompositions for high dimensional data, as described in
<http://arxiv.org/abs/1405.0922>. For data matrices that are too large to
operate on in memory, users can input objects with class 'ff' (see the
'ff' package), where the actual data is stored on disk. In response, this
package will implement a block matrix algebra procedure for calculating
the principal components (PCs) and bootstrap PCs. Depending on options set
by the user, the 'parallel' package can be used to parallelize the
calculation of the bootstrap PCs.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
