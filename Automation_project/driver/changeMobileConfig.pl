#!/usr/local/bin/perl

use Cwd;
$workspace=getcwd();

$prodid = shift(@ARGV);
$confid = shift(@ARGV);
$relid = shift(@ARGV);
$browser=shift(@ARGV);
$suiteFolder=shift(@ARGV);
$device=shift(@ARGV);

print $device;
my $os;
$suiteFolder= "$workspace/qa/selenium/${suiteFolder}";
my $Conf = {};
$initFile=$suiteFolder."/config.init";

print "$initFile\n";

my @resp = qx(perl qa/selenium/driver/getconf.pl $prodid $confid $relid);
chomp(@resp);
foreach my $resp (@resp) {
    my ($key,$val) = $resp =~ /^(\S+)\s+(.+)$/;
    $Conf->{$key} = $val;
}

my $device_id;
my $device_name;
my $device_version;

if ($device eq 'android'){
	$device_id="015d46d9271c1015";
	$device_name="Nexus 7";
	$device_version="5.1.1";
}elsif($device eq 'ios'){
	$device_id="8023dbe164a74b8ddff9d58ce06b8408cb37f945";
	$device_name="Douglas's iPad (2)";
	$device_version="11.1";
}

if ($browser eq 'ff'){
   $browser='Firefox';
  }elsif($browser eq 'ie'){
    $browser='IE';
   $browser_driver='D:\IEDriverServer.exe';
  }elsif($browser eq 'cr'){
   $browser='Chrome';
   $os='android';
   $browser_driver='/usr/local/lib/driver/chromedriver';
  }elsif($browser eq 'sf'){
   $browser='Safari';
   $os='ios';
  }elsif($browser eq 'eg'){
   $browser='Edge';
   $browser_driver='D:\MicrosoftWebDriver.exe';
  }
  
$nodeid=$Conf->{nodeid};
$wfnode=$Conf->{wfnode};
$httpport=$Conf->{httpport};
$wfcontext=$Conf->{wfcontext};
#$mrid=$Conf->{mrid};
#$mrpass=$Conf->{mrpass};


open(FILE, $initFile) || die "File not found";
my @lines = <FILE>;
close(FILE);
my $test;
for ($i=0;$i<scalar @lines;$i++){
$temp=@lines[$i];
$temp=~ s/^\s+|\s+$//g;
if ($temp eq 'test web'){
$test=$os.'_web';
}
elsif($temp eq 'test app'){
$test=$os.'_app';
}
}

my @newlines;
foreach(@lines) {
   $_ =~ s/nodeid\s+(.+)/nodeid $nodeid/;
   $_ =~ s/httpport\s+(.+)/httpport $httpport/;
   $_ =~ s/wfcontext\s+(.+)/wfcontext $wfcontext/;
   $_ =~ s/browser\s+(.+)/browser $browser/;
   $_ =~ s/browser_driver\s+(.+)/browser_driver $browser_driver/;
   $_ =~ s/test\s+(.+)/test $test/;
   $_ =~ s/device\s+(.+)/device $device/;
   $_ =~ s/device_id\s+(.+)/device_id $device_id/;
   $_ =~ s/device_name\s+(.+)/device_name $device_name/;
   $_ =~ s/device_version\s+(.+)/device_version $device_version/;
   push(@newlines,$_);
}

open(FILE, ">$initFile") || die "File not found";
print FILE @newlines;
close(FILE);
