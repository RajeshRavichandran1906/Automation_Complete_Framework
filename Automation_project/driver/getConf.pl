#!/usr/local/bin/perl

use English;
use FindBin;
use lib $FindBin::Bin;
use Procsrv qw($cgiBin);
my ($T,$F) = (1,0);

sub usage {
    print("$ARG[0]\n") if (@ARG > 0);
    print(qq^
usage: getConf.pl [-section <section>] [-keepcase] <prodid> <confid> <relid>
  prints target <confid> configuration top-level keys and release
  <relid> configuration keys (target has precedence), else, 
  <section> is present, just that section of the target config.
  Keys will be lower-cased, unless '-keepcase' is present.
  Either of <confid> and <relid> can be '-'.
^);
    exit(1);
}
my $section = undef;
my $keepcase = $F;
while (@ARGV > 0 and $ARGV[0] =~ /^-/) {
    my $sw = shift(@ARGV);
    if ($sw eq '-section'){
	$section = shift(@ARGV);
    } elsif ($sw eq '-keepcase') {
	$keepcase = $T;
    } else {
	usage("ERROR: (getConf.pl) unrecognized switch '$sw'");
    }
}
my ($prodid,$confid,$relid,$extra) = @ARGV;
usage() if (defined $extra or not defined $relid);
my $tmpfi = (($OSNAME eq 'MSWin32') ? "C:\\temp\\" : "/tmp/") .
    "getConf.o.$PID";
my $url = "$cgiBin/confCgi.pl" .
    "?prodid=$prodid&confid=$confid&relid=$relid";
$url .= "&section=$section" if (defined $section);
$url .= "&keepcase=true" if ($keepcase);
my $cmd = "wget -o $tmpfi -O - \"$url\"";
my @resp = qx($cmd);
my $rc = $CHILD_ERROR>>8;
if ($rc) {
    print("ERROR: (getConf.pl):");
    if ($OSNAME eq 'MSWin32') {
	system("type $tmpfi");
    } else {
	system("cat $tmpfi");
    }
    unlink($tmpfi);
    exit(1);
}
unlink($tmpfi);
my ($err) = $resp[0] =~ /^ERROR:(.*)$/;
if (defined $err) {
    print("ERROR: $err\n");
    exit(1);
}
print(@resp);
exit(0);
