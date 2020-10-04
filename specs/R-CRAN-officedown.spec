%global packname  officedown
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}%{?buildtag}
Summary:          Enhanced 'R Markdown' Format for 'Word' and 'PowerPoint'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-officer >= 0.3.12
BuildRequires:    R-CRAN-rvg >= 0.2.2
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-officer >= 0.3.12
Requires:         R-CRAN-rvg >= 0.2.2
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-uuid 
Requires:         R-grDevices 
Requires:         R-CRAN-yaml 
Requires:         R-utils 
Requires:         R-CRAN-memoise 

%description
Allows production of 'Microsoft' corporate documents from 'R Markdown' by
reusing formatting defined in 'Microsoft Word' documents. You can reuse
table styles, list styles but also add column sections, landscape oriented
pages. Table and image captions as well as cross-references are
transformed into 'Microsoft Word' fields, allowing documents edition and
merging without issue with references; the syntax conforms to the
'bookdown' cross-reference definition. Objects generated by the 'officer'
package are also supported in the 'knitr' chunks. 'Microsoft PowerPoint'
presentations also benefit from this as well as the ability to produce
editable vector graphics in 'PowerPoint' and also to define placeholder
where content is to be added.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
