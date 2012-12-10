%define _requires_exceptions pear(class\\|pear(odbcsocketserver.class.php)\\|pear(smartypants.php)\\|perl(AlgParser)\\|pear(domxml-php4-to-php5.php)

%undefine __find_provides

Summary:    A course management system for distance education
Name:       moodle
Version:    2.2
Release:    %mkrel 1
License:    GPLv2
Group:      System/Servers
URL:        http://moodle.org/
Source0:    http://download.moodle.org/stable19/%{name}-%{version}.tgz

Source2:    http://download.moodle.org/lang16/af_utf8.zip
Source3:    http://download.moodle.org/lang16/sq_utf8.zip
Source4:    http://download.moodle.org/lang16/ar_utf8.zip
Source5:    http://download.moodle.org/lang16/eu_utf8.zip
Source6:    http://download.moodle.org/lang16/be_utf8.zip
Source7:    http://download.moodle.org/lang16/bs_utf8.zip
Source8:    http://download.moodle.org/lang16/bg_utf8.zip
Source9:    http://download.moodle.org/lang16/ca_utf8.zip
Source10:   http://download.moodle.org/lang16/hr_utf8.zip
Source11:   http://download.moodle.org/lang16/zh_cn_utf8.zip
Source12:   http://download.moodle.org/lang16/zh_tw_utf8.zip
Source13:   http://download.moodle.org/lang16/cs_utf8.zip
Source14:   http://download.moodle.org/lang16/da_utf8.zip
Source15:   http://download.moodle.org/lang16/nl_utf8.zip
Source16:   http://download.moodle.org/lang16/en_us_utf8.zip
Source17:   http://download.moodle.org/lang16/et_utf8.zip
Source18:   http://download.moodle.org/lang16/fa_utf8.zip
Source19:   http://download.moodle.org/lang16/fil_utf8.zip
Source20:   http://download.moodle.org/lang16/fi_utf8.zip
Source21:   http://download.moodle.org/lang16/fr_utf8.zip
Source22:   http://download.moodle.org/lang16/fr_ca_utf8.zip
Source23:   http://download.moodle.org/lang16/ga_utf8.zip
Source24:   http://download.moodle.org/lang16/gl_utf8.zip
Source25:   http://download.moodle.org/lang16/ka_utf8.zip
Source26:   http://download.moodle.org/lang16/de_utf8.zip
Source27:   http://download.moodle.org/lang16/de_du_utf8.zip
Source28:   http://download.moodle.org/lang16/el_utf8.zip
Source29:   http://download.moodle.org/lang16/gu_utf8.zip
Source30:   http://download.moodle.org/lang16/he_utf8.zip
Source31:   http://download.moodle.org/lang16/hi_utf8.zip
Source32:   http://download.moodle.org/lang16/hu_utf8.zip
Source33:   http://download.moodle.org/lang16/is_utf8.zip
Source34:   http://download.moodle.org/lang16/id_utf8.zip
Source35:   http://download.moodle.org/lang16/it_utf8.zip
Source36:   http://download.moodle.org/lang16/ja_utf8.zip
Source37:   http://download.moodle.org/lang16/kn_utf8.zip
Source38:   http://download.moodle.org/lang16/km_utf8.zip
Source39:   http://download.moodle.org/lang16/ko_utf8.zip
Source40:   http://download.moodle.org/lang16/lt_utf8.zip
Source41:   http://download.moodle.org/lang16/lo_utf8.zip
Source42:   http://download.moodle.org/lang16/lv_utf8.zip
Source43:   http://download.moodle.org/lang16/ml_utf8.zip
Source44:   http://download.moodle.org/lang16/ms_utf8.zip
Source45:   http://download.moodle.org/lang16/mi_tn_utf8.zip
Source46:   http://download.moodle.org/lang16/mi_wwow_utf8.zip
Source47:   http://download.moodle.org/lang16/mn_utf8.zip
Source48:   http://download.moodle.org/lang16/no_utf8.zip
Source49:   http://download.moodle.org/lang16/no_gr_utf8.zip
Source50:   http://download.moodle.org/lang16/nn_utf8.zip
Source51:   http://download.moodle.org/lang16/pl_utf8.zip
Source52:   http://download.moodle.org/lang16/pt_utf8.zip
Source53:   http://download.moodle.org/lang16/pt_br_utf8.zip
Source54:   http://download.moodle.org/lang16/ro_utf8.zip
Source55:   http://download.moodle.org/lang16/ru_utf8.zip
Source56:   http://download.moodle.org/lang16/sm_utf8.zip
Source57:   http://download.moodle.org/lang16/si_utf8.zip
Source58:   http://download.moodle.org/lang16/sr_cr_bo_utf8.zip
Source59:   http://download.moodle.org/lang16/sr_cr_utf8.zip
Source60:   http://download.moodle.org/lang16/sr_lt_utf8.zip
Source61:   http://download.moodle.org/lang16/sk_utf8.zip
Source62:   http://download.moodle.org/lang16/sl_utf8.zip
Source63:   http://download.moodle.org/lang16/so_utf8.zip
Source64:   http://download.moodle.org/lang16/es_utf8.zip
Source65:   http://download.moodle.org/lang16/sv_utf8.zip
Source66:   http://download.moodle.org/lang16/tl_utf8.zip
Source67:   http://download.moodle.org/lang16/ta_utf8.zip
Source68:   http://download.moodle.org/lang16/th_utf8.zip
Source69:   http://download.moodle.org/lang16/to_utf8.zip
Source70:   http://download.moodle.org/lang16/tr_utf8.zip
Source71:   http://download.moodle.org/lang16/uk_utf8.zip
Source72:   http://download.moodle.org/lang16/vi_utf8.zip
Source73:   http://download.moodle.org/lang16/dv_utf8.zip
Source74:   http://download.moodle.org/lang16/cy_utf8.zip                              
Source75:   http://download.moodle.org/lang16/en_utf8.zip                              
Source76:   http://download.moodle.org/lang16/mr_utf8.zip                              
Source77:   http://download.moodle.org/lang16/ur_utf8.zip                              
Source78:   http://download.moodle.org/lang16/ast_utf8.zip                              
Source79:   http://download.moodle.org/lang16/la_utf8.zip                              
Source80:   http://download.moodle.org/lang16/uz_utf8.zip                              
Source81:   http://download.moodle.org/lang16/kk_utf8.zip                              
Source82:   http://download.moodle.org/lang16/mk_utf8.zip                              
Source83:   http://download.moodle.org/lang16/hy_utf8.zip                              
Source84:   http://download.moodle.org/lang16/ta_lk_utf8.zip                              
Source85:   http://download.moodle.org/lang16/zu_utf8.zip                              
Source86:   http://download.moodle.org/lang16/bn_utf8.zip                              


Patch0:     moodle-external_mimetex.diff
Patch1:     moodle-1.9.4-CVE-2009-1171.diff

Requires:	php-curl
Requires:	php-gd
Requires:	php-iconv
Requires:	php-ldap
Requires:	php-mbstring
Requires:	php-mysql
Requires:	php-openssl
Requires:	php-pgsql
Requires:	php-sockets
Requires:	php-tidy
Requires:	php-tokenizer
Requires:	php-xml
Requires:	php-zlib

Requires:	imagemagick
Requires:	mimetex
Requires:	tetex-dvips
Requires:	tetex-latex

%if %mdkversion < 201010
Requires(post):   rpm-helper
Requires(postun):   rpm-helper
%endif

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Moodle is a learning management system for producing Internet-based course Web
sites. It is written in PHP and is easy to install and use on Linux, Windows,
Mac OS X, SunOS, BSD, and Netware 6. It has been designed to support modern
pedagogies based on social constructionist theory, and includes activity
modules such as forums, chats, resources, journals, quizzes, surveys, choices,
workshops, glossaries, lessons, and assignments. It has been translated into
over 70 languages, with more on the way, and supports the popular SCORM
standard for content packaging. Moodle offers a free alternative to commercial
software such as WebCT or Blackboard, and is being used by a growing number of
universities, schools, and independent teachers for distance education or to
supplement face-to-face teaching.

%prep

%setup -q -n %{name}
#%patch0 -p0
#%patch1 -p0

# magic by anssi
pushd lang; %{expand:%(for i in {2..86}; do echo "unzip -q %%SOURCE$i"; done)}; popd

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

# fix dir perms
find . -type d | xargs chmod 755

# fix file perms
find . -type f -print0 | xargs --null chmod 644

# nuke bundled stuff
rm -rf lib/pear
rm -f filter/tex/mimetex.*

# set some exec bits
chmod 755 filter/algebra/algebra2tex.pl

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d
install -d %{buildroot}%{_sysconfdir}/%{name}
install -d %{buildroot}/var/www/%{name}
install -d %{buildroot}/var/moodledata

cp -aRf * %{buildroot}/var/www/%{name}/

# apache config
cat > %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf << EOF

Alias /%{name} /var/www/%{name}

<Directory /var/www/%{name}>
    Allow from All

    # On some PHP servers it may help if this file is copied
    # to the main moodle directory and renamed .htaccess
    #
    # As soon as you do this, check your web site.  Is it 
    # still working OK?  If you are getting a "configuration
    # error" then you may need to enable overrides by editing
    # the main httpd.conf for Apache and in the main server
    # or virtual server area, adding something like:
    #
    # <Directory /web/moodle>
    #     AllowOverride All 
    # </Directory>
    #

    ### Firstly, if you are using Apache 2, you need the following
    ### line to allow Apache to pass a PATH_INFO variable 
    ### correctly for URLs like http://server/file.php/arg1/arg2
    AcceptPathInfo on

    ### Secondly, you can define the default files in the Moodle
    ### directories as follows:

    DirectoryIndex index.php index.html index.htm

    ### Thirdly, set up some PHP variables that Moodle needs
    php_admin_value magic_quotes_gpc		1
    php_admin_value magic_quotes_runtime	0
    php_admin_value register_globals		0
    php_admin_value file_uploads		1
    php_admin_value short_open_tag		1
    php_admin_value session.auto_start		0
    php_admin_value session.bug_compat_warn	0

    php_admin_value safe_mode			0
    php_admin_value memory_limit		64M
    php_admin_value session.save_handler	files

    ### Fourthly, sometimes Apache limits the size of uploaded files
    ### (this is a separate limit to the one in PHP, see below).
    ### The setting here turns off this limitation
    LimitRequestBody 0

    ### These are optional - you may not want to override php.ini 
    ### To enable them, remove the leading hash (#)
    php_admin_value upload_max_filesize		2M
    php_admin_value post_max_size		2M
    php_admin_value session.gc_maxlifetime	7200

    ### You can change the following line to point to the 
    ### error/index.php file in your Moodle distribution.  
    ### It provides a form which emails you (the admin) 
    ### about 404 errors (URL not found).
    #ErrorDocument 404 http://example.org/moodle/error/index.php

    ### People have reported that these can help in some cases
    ### (unusual) when you see errors about undefined functions
    #php_admin_value auto_prepend_file		none
    #php_admin_value include_path		.

</Directory>

<Directory /var/www/%{name}/install>
    Order deny,allow
    Deny from all
    Allow from 127.0.0.1
    ErrorDocument 403 "Access denied per %{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf"
 </Directory>

<FilesMatch install.php>
    Order deny,allow
    Deny from all
    Allow from 127.0.0.1
    ErrorDocument 403 "Access denied per %{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf"
</FilesMatch>

EOF

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201010
%_post_webapp
%endif

%postun
%if %mdkversion < 201010
%_postun_webapp
%endif

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf
/var/www/%{name}
%attr(2777,apache,apache) %dir /var/moodledata


%changelog
* Mon Dec 12 2011 Sergey Zhemoitel <serg@mandriva.org> 2.2-1mdv2012.0
+ Revision: 740588
- add new version 2.2

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.9-2mdv2011.0
+ Revision: 612929
- the mass rebuild of 2010.1 packages

  + Jerome Martin <jmartin@mandriva.org>
    - Version 1.9.9

* Sun Feb 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.5-2mdv2010.1
+ Revision: 509213
- rely on filetrigger for reloading apache configuration begining with 2010.1, rpm-helper macros otherwise

* Fri Jul 31 2009 Frederik Himpe <fhimpe@mandriva.org> 1.9.5-1mdv2010.0
+ Revision: 405256
- update to new version 1.9.5

* Tue Mar 31 2009 Oden Eriksson <oeriksson@mandriva.com> 1.9.4-2mdv2009.1
+ Revision: 362835
- bump release
- P1: security fix for CVE-2009-1171

* Tue Feb 17 2009 Jerome Martin <jmartin@mandriva.org> 1.9.4-1mdv2009.1
+ Revision: 341165
- 1.9.4

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Oct 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.9.3-1mdv2009.1
+ Revision: 294420
- 1.9.3
- new S2 - S72

* Sat Sep 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.9.2-1mdv2009.0
+ Revision: 281928
- 1.9.2
- new S2 - S72
- rediffed P0

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.8.2-3mdv2009.0
+ Revision: 252776
- rebuild

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 1.8.2-1mdv2008.1
+ Revision: 140955
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Oden Eriksson <oeriksson@mandriva.com> 1.8.2-1mdv2008.0
+ Revision: 68635
- Import moodle

