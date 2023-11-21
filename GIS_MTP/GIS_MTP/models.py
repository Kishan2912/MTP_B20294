from django.contrib.gis.db import models

class GIS(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    geom = models.MultiPolygonField()

    class Meta:
        db_table = 'shape_tb'
        indexes = [models.Index(fields=['geom'])]

class GIS_District(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.SmallIntegerField()
    statecode = models.CharField(max_length=2)
    statename = models.CharField(max_length=50)
    state_ut = models.CharField(max_length=2)
    distcode = models.CharField(max_length=4)
    distname = models.CharField(max_length=50)
    distarea = models.IntegerField()
    totalpopul = models.IntegerField()
    totalhh = models.IntegerField()
    totpopmale = models.IntegerField()
    totpopfema = models.IntegerField()
    st_areasha = models.FloatField()
    st_lengths = models.FloatField()
    geom = models.MultiPolygonField()

    class Meta:
        db_table = 'district_shape_file'
        indexes = [models.Index(fields=['geom'])]


class DistrictData(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    nainital = models.FloatField(db_column='Nainital', blank=True, null=True)  # Field name made lowercase.
    dehradun = models.FloatField(db_column='Dehradun', blank=True, null=True)  # Field name made lowercase.
    almora = models.FloatField(db_column='Almora', blank=True, null=True)  # Field name made lowercase.
    champawat = models.FloatField(db_column='Champawat', blank=True, null=True)  # Field name made lowercase.
    uttarkashi = models.FloatField(db_column='Uttarkashi', blank=True, null=True)  # Field name made lowercase.
    garhwal = models.FloatField(db_column='Garhwal', blank=True, null=True)  # Field name made lowercase.
    hardwar = models.FloatField(db_column='Hardwar', blank=True, null=True)  # Field name made lowercase.
    rudraprayag = models.FloatField(db_column='Rudraprayag', blank=True, null=True)  # Field name made lowercase.
    tehri_garhwal = models.FloatField(db_column='Tehri Garhwal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bageshwar = models.FloatField(db_column='Bageshwar', blank=True, null=True)  # Field name made lowercase.
    pithoragarh = models.FloatField(db_column='Pithoragarh', blank=True, null=True)  # Field name made lowercase.
    chamoli = models.FloatField(db_column='Chamoli', blank=True, null=True)  # Field name made lowercase.
    udham_singh_nagar = models.FloatField(db_column='Udham Singh Nagar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chamba = models.FloatField(db_column='Chamba', blank=True, null=True)  # Field name made lowercase.
    shimla = models.FloatField(db_column='Shimla', blank=True, null=True)  # Field name made lowercase.
    bilaspur = models.FloatField(db_column='Bilaspur', blank=True, null=True)  # Field name made lowercase.
    kangra = models.FloatField(db_column='Kangra', blank=True, null=True)  # Field name made lowercase.
    lahul_spiti = models.FloatField(db_column='Lahul & Spiti', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    una = models.FloatField(db_column='Una', blank=True, null=True)  # Field name made lowercase.
    solan = models.FloatField(db_column='Solan', blank=True, null=True)  # Field name made lowercase.
    sirmaur = models.FloatField(db_column='Sirmaur', blank=True, null=True)  # Field name made lowercase.
    kinnaur = models.FloatField(db_column='Kinnaur', blank=True, null=True)  # Field name made lowercase.
    mandi = models.FloatField(db_column='Mandi', blank=True, null=True)  # Field name made lowercase.
    kullu = models.FloatField(db_column='Kullu', blank=True, null=True)  # Field name made lowercase.
    bhind = models.FloatField(db_column='Bhind', blank=True, null=True)  # Field name made lowercase.
    jhabua = models.FloatField(db_column='Jhabua', blank=True, null=True)  # Field name made lowercase.
    seoni = models.FloatField(db_column='Seoni', blank=True, null=True)  # Field name made lowercase.
    khandwa_east_nimar = models.FloatField(db_column='Khandwa (East Nimar)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    umaria = models.FloatField(db_column='Umaria', blank=True, null=True)  # Field name made lowercase.
    hamirpur = models.FloatField(db_column='Hamirpur', blank=True, null=True)  # Field name made lowercase.
    data_not_available = models.FloatField(db_column='DATA NOT AVAILABLE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anantnag = models.FloatField(db_column='Anantnag', blank=True, null=True)  # Field name made lowercase.
    baramula = models.FloatField(db_column='Baramula', blank=True, null=True)  # Field name made lowercase.
    kulgam = models.FloatField(db_column='Kulgam', blank=True, null=True)  # Field name made lowercase.
    shupiyan = models.FloatField(db_column='Shupiyan', blank=True, null=True)  # Field name made lowercase.
    reasi = models.FloatField(db_column='Reasi', blank=True, null=True)  # Field name made lowercase.
    rajouri = models.FloatField(db_column='Rajouri', blank=True, null=True)  # Field name made lowercase.
    jammu = models.FloatField(db_column='Jammu', blank=True, null=True)  # Field name made lowercase.
    srinagar = models.FloatField(db_column='Srinagar', blank=True, null=True)  # Field name made lowercase.
    punch = models.FloatField(db_column='Punch', blank=True, null=True)  # Field name made lowercase.
    kupwara = models.FloatField(db_column='Kupwara', blank=True, null=True)  # Field name made lowercase.
    samba = models.FloatField(db_column='Samba', blank=True, null=True)  # Field name made lowercase.
    bandipore = models.FloatField(db_column='Bandipore', blank=True, null=True)  # Field name made lowercase.
    kathua = models.FloatField(db_column='Kathua', blank=True, null=True)  # Field name made lowercase.
    kishtwar = models.FloatField(db_column='Kishtwar', blank=True, null=True)  # Field name made lowercase.
    sabar_kantha = models.FloatField(db_column='Sabar Kantha', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    banas_kantha = models.FloatField(db_column='Banas Kantha', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    surendranagar = models.FloatField(db_column='Surendranagar', blank=True, null=True)  # Field name made lowercase.
    anand = models.FloatField(db_column='Anand', blank=True, null=True)  # Field name made lowercase.
    narmada = models.FloatField(db_column='Narmada', blank=True, null=True)  # Field name made lowercase.
    amreli = models.FloatField(db_column='Amreli', blank=True, null=True)  # Field name made lowercase.
    dohad = models.FloatField(db_column='Dohad', blank=True, null=True)  # Field name made lowercase.
    doda = models.FloatField(db_column='Doda', blank=True, null=True)  # Field name made lowercase.
    pulwama = models.FloatField(db_column='Pulwama', blank=True, null=True)  # Field name made lowercase.
    vadodara = models.FloatField(db_column='Vadodara', blank=True, null=True)  # Field name made lowercase.
    aravali = models.FloatField(db_column='Aravali', blank=True, null=True)  # Field name made lowercase.
    gwalior = models.FloatField(db_column='Gwalior', blank=True, null=True)  # Field name made lowercase.
    damoh = models.FloatField(db_column='Damoh', blank=True, null=True)  # Field name made lowercase.
    dhar = models.FloatField(db_column='Dhar', blank=True, null=True)  # Field name made lowercase.
    katni = models.FloatField(db_column='Katni', blank=True, null=True)  # Field name made lowercase.
    sidhi = models.FloatField(db_column='Sidhi', blank=True, null=True)  # Field name made lowercase.
    alirajpur = models.FloatField(db_column='Alirajpur', blank=True, null=True)  # Field name made lowercase.
    singrauli = models.FloatField(db_column='Singrauli', blank=True, null=True)  # Field name made lowercase.
    bhopal = models.FloatField(db_column='Bhopal', blank=True, null=True)  # Field name made lowercase.
    ramban = models.FloatField(db_column='Ramban', blank=True, null=True)  # Field name made lowercase.
    ganderbal = models.FloatField(db_column='Ganderbal', blank=True, null=True)  # Field name made lowercase.
    udhampur = models.FloatField(db_column='Udhampur', blank=True, null=True)  # Field name made lowercase.
    badgam = models.FloatField(db_column='Badgam', blank=True, null=True)  # Field name made lowercase.
    rajgarh = models.FloatField(db_column='Rajgarh', blank=True, null=True)  # Field name made lowercase.
    mandla = models.FloatField(db_column='Mandla', blank=True, null=True)  # Field name made lowercase.
    shajapur = models.FloatField(db_column='Shajapur', blank=True, null=True)  # Field name made lowercase.
    shivpuri = models.FloatField(db_column='Shivpuri', blank=True, null=True)  # Field name made lowercase.
    datia = models.FloatField(db_column='Datia', blank=True, null=True)  # Field name made lowercase.
    shahdol = models.FloatField(db_column='Shahdol', blank=True, null=True)  # Field name made lowercase.
    vidisha = models.FloatField(db_column='Vidisha', blank=True, null=True)  # Field name made lowercase.
    prakasam = models.FloatField(db_column='Prakasam', blank=True, null=True)  # Field name made lowercase.
    krishna = models.FloatField(db_column='Krishna', blank=True, null=True)  # Field name made lowercase.
    hugli = models.FloatField(db_column='Hugli', blank=True, null=True)  # Field name made lowercase.
    ambedkar_nagar = models.FloatField(db_column='Ambedkar Nagar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ballia = models.FloatField(db_column='Ballia', blank=True, null=True)  # Field name made lowercase.
    kanpur_nagar = models.FloatField(db_column='Kanpur Nagar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sant_ravidas_nagar_bhadohi_field = models.FloatField(db_column='Sant Ravidas Nagar (Bhadohi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    daman = models.FloatField(db_column='Daman', blank=True, null=True)  # Field name made lowercase.
    diu = models.FloatField(db_column='Diu', blank=True, null=True)  # Field name made lowercase.
    bhavnagar = models.FloatField(db_column='Bhavnagar', blank=True, null=True)  # Field name made lowercase.
    ahmadabad = models.FloatField(db_column='Ahmadabad', blank=True, null=True)  # Field name made lowercase.
    chhota_udaipur = models.FloatField(db_column='Chhota Udaipur', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    batod = models.FloatField(db_column='Batod', blank=True, null=True)  # Field name made lowercase.
    rajkot = models.FloatField(db_column='Rajkot', blank=True, null=True)  # Field name made lowercase.
    kachchh = models.FloatField(db_column='Kachchh', blank=True, null=True)  # Field name made lowercase.
    kurnool = models.FloatField(db_column='Kurnool', blank=True, null=True)  # Field name made lowercase.
    guntur = models.FloatField(db_column='Guntur', blank=True, null=True)  # Field name made lowercase.
    vizianagaram = models.FloatField(db_column='Vizianagaram', blank=True, null=True)  # Field name made lowercase.
    anantapur = models.FloatField(db_column='Anantapur', blank=True, null=True)  # Field name made lowercase.
    west_godavari = models.FloatField(db_column='West Godavari', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kadapa_ysr = models.FloatField(db_column='Kadapa(YSR)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    kannur = models.FloatField(db_column='Kannur', blank=True, null=True)  # Field name made lowercase.
    pathanamthitta = models.FloatField(db_column='Pathanamthitta', blank=True, null=True)  # Field name made lowercase.
    alappuzha = models.FloatField(db_column='Alappuzha', blank=True, null=True)  # Field name made lowercase.
    ernakulam = models.FloatField(db_column='Ernakulam', blank=True, null=True)  # Field name made lowercase.
    kollam = models.FloatField(db_column='Kollam', blank=True, null=True)  # Field name made lowercase.
    kasaragod = models.FloatField(db_column='Kasaragod', blank=True, null=True)  # Field name made lowercase.
    idukki = models.FloatField(db_column='Idukki', blank=True, null=True)  # Field name made lowercase.
    the_dangs = models.FloatField(db_column='The Dangs', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mahesana = models.FloatField(db_column='Mahesana', blank=True, null=True)  # Field name made lowercase.
    patan = models.FloatField(db_column='Patan', blank=True, null=True)  # Field name made lowercase.
    bharuch = models.FloatField(db_column='Bharuch', blank=True, null=True)  # Field name made lowercase.
    gir_somnath = models.FloatField(db_column='Gir Somnath', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    junagadh = models.FloatField(db_column='Junagadh', blank=True, null=True)  # Field name made lowercase.
    devbhumi_dwarka = models.FloatField(db_column='Devbhumi Dwarka', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    navsari = models.FloatField(db_column='Navsari', blank=True, null=True)  # Field name made lowercase.
    surat = models.FloatField(db_column='Surat', blank=True, null=True)  # Field name made lowercase.
    jamnagar = models.FloatField(db_column='Jamnagar', blank=True, null=True)  # Field name made lowercase.
    tapi = models.FloatField(db_column='Tapi', blank=True, null=True)  # Field name made lowercase.
    kheda = models.FloatField(db_column='Kheda', blank=True, null=True)  # Field name made lowercase.
    betul = models.FloatField(db_column='Betul', blank=True, null=True)  # Field name made lowercase.
    hoshangabad = models.FloatField(db_column='Hoshangabad', blank=True, null=True)  # Field name made lowercase.
    sehore = models.FloatField(db_column='Sehore', blank=True, null=True)  # Field name made lowercase.
    jabalpur = models.FloatField(db_column='Jabalpur', blank=True, null=True)  # Field name made lowercase.
    narsimhapur = models.FloatField(db_column='Narsimhapur', blank=True, null=True)  # Field name made lowercase.
    panna = models.FloatField(db_column='Panna', blank=True, null=True)  # Field name made lowercase.
    ujjain = models.FloatField(db_column='Ujjain', blank=True, null=True)  # Field name made lowercase.
    rewa = models.FloatField(db_column='Rewa', blank=True, null=True)  # Field name made lowercase.
    dindori = models.FloatField(db_column='Dindori', blank=True, null=True)  # Field name made lowercase.
    balaghat = models.FloatField(db_column='Balaghat', blank=True, null=True)  # Field name made lowercase.
    barwani = models.FloatField(db_column='Barwani', blank=True, null=True)  # Field name made lowercase.
    porbandar = models.FloatField(db_column='Porbandar', blank=True, null=True)  # Field name made lowercase.
    valsad = models.FloatField(db_column='Valsad', blank=True, null=True)  # Field name made lowercase.
    gandhinagar = models.FloatField(db_column='Gandhinagar', blank=True, null=True)  # Field name made lowercase.
    mahisagar = models.FloatField(db_column='Mahisagar', blank=True, null=True)  # Field name made lowercase.
    morbi = models.FloatField(db_column='Morbi', blank=True, null=True)  # Field name made lowercase.
    panch_mahals = models.FloatField(db_column='Panch Mahals', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kozhikode = models.FloatField(db_column='Kozhikode', blank=True, null=True)  # Field name made lowercase.
    kottayam = models.FloatField(db_column='Kottayam', blank=True, null=True)  # Field name made lowercase.
    thrissur = models.FloatField(db_column='Thrissur', blank=True, null=True)  # Field name made lowercase.
    palakkad = models.FloatField(db_column='Palakkad', blank=True, null=True)  # Field name made lowercase.
    thiruvananthapuram = models.FloatField(db_column='Thiruvananthapuram', blank=True, null=True)  # Field name made lowercase.
    malappuram = models.FloatField(db_column='Malappuram', blank=True, null=True)  # Field name made lowercase.
    wayanad = models.FloatField(db_column='Wayanad', blank=True, null=True)  # Field name made lowercase.
    lakshadweep = models.FloatField(db_column='Lakshadweep', blank=True, null=True)  # Field name made lowercase.
    north_district = models.FloatField(db_column='North District', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sheikhpura = models.FloatField(db_column='Sheikhpura', blank=True, null=True)  # Field name made lowercase.
    jehanabad = models.FloatField(db_column='Jehanabad', blank=True, null=True)  # Field name made lowercase.
    saharsa = models.FloatField(db_column='Saharsa', blank=True, null=True)  # Field name made lowercase.
    dadra_nagar_haveli = models.FloatField(db_column='Dadra & Nagar Haveli', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ashoknagar = models.FloatField(db_column='Ashoknagar', blank=True, null=True)  # Field name made lowercase.
    raisen = models.FloatField(db_column='Raisen', blank=True, null=True)  # Field name made lowercase.
    chhindwara = models.FloatField(db_column='Chhindwara', blank=True, null=True)  # Field name made lowercase.
    patna = models.FloatField(db_column='Patna', blank=True, null=True)  # Field name made lowercase.
    satna = models.FloatField(db_column='Satna', blank=True, null=True)  # Field name made lowercase.
    chhatarpur = models.FloatField(db_column='Chhatarpur', blank=True, null=True)  # Field name made lowercase.
    indore = models.FloatField(db_column='Indore', blank=True, null=True)  # Field name made lowercase.
    ratlam = models.FloatField(db_column='Ratlam', blank=True, null=True)  # Field name made lowercase.
    harda = models.FloatField(db_column='Harda', blank=True, null=True)  # Field name made lowercase.
    sagar = models.FloatField(db_column='Sagar', blank=True, null=True)  # Field name made lowercase.
    neemuch = models.FloatField(db_column='Neemuch', blank=True, null=True)  # Field name made lowercase.
    tikamgarh = models.FloatField(db_column='Tikamgarh', blank=True, null=True)  # Field name made lowercase.
    guna = models.FloatField(db_column='Guna', blank=True, null=True)  # Field name made lowercase.
    dewas = models.FloatField(db_column='Dewas', blank=True, null=True)  # Field name made lowercase.
    mandsaur = models.FloatField(db_column='Mandsaur', blank=True, null=True)  # Field name made lowercase.
    khargone_west_nimar_field = models.FloatField(db_column='Khargone (West Nimar)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sheopur = models.FloatField(db_column='Sheopur', blank=True, null=True)  # Field name made lowercase.
    morena = models.FloatField(db_column='Morena', blank=True, null=True)  # Field name made lowercase.
    burhanpur = models.FloatField(db_column='Burhanpur', blank=True, null=True)  # Field name made lowercase.
    anuppur = models.FloatField(db_column='Anuppur', blank=True, null=True)  # Field name made lowercase.
    east_godavari = models.FloatField(db_column='East Godavari', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    visakhapatnam = models.FloatField(db_column='Visakhapatnam', blank=True, null=True)  # Field name made lowercase.
    sri_potti_sriramulu_nellore = models.FloatField(db_column='Sri Potti Sriramulu Nellore', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chittoor = models.FloatField(db_column='Chittoor', blank=True, null=True)  # Field name made lowercase.
    srikakulam = models.FloatField(db_column='Srikakulam', blank=True, null=True)  # Field name made lowercase.
    east_district = models.FloatField(db_column='East District', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nadia = models.FloatField(db_column='Nadia', blank=True, null=True)  # Field name made lowercase.
    dakshin_dinajpur = models.FloatField(db_column='Dakshin Dinajpur', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    south_district = models.FloatField(db_column='South District', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    murshidabad = models.FloatField(db_column='Murshidabad', blank=True, null=True)  # Field name made lowercase.
    barddhaman = models.FloatField(db_column='Barddhaman', blank=True, null=True)  # Field name made lowercase.
    bankura = models.FloatField(db_column='Bankura', blank=True, null=True)  # Field name made lowercase.
    puruliya = models.FloatField(db_column='Puruliya', blank=True, null=True)  # Field name made lowercase.
    koch_bihar = models.FloatField(db_column='Koch Bihar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    paschim_medinipur = models.FloatField(db_column='Paschim Medinipur', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    west_district = models.FloatField(db_column='West District', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kolkata = models.FloatField(db_column='Kolkata', blank=True, null=True)  # Field name made lowercase.
    maldah = models.FloatField(db_column='Maldah', blank=True, null=True)  # Field name made lowercase.
    south_twenty_four_parganas = models.FloatField(db_column='South Twenty Four Parganas', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    darjiling = models.FloatField(db_column='Darjiling', blank=True, null=True)  # Field name made lowercase.
    jalpaiguri = models.FloatField(db_column='Jalpaiguri', blank=True, null=True)  # Field name made lowercase.
    uttar_dinajpur = models.FloatField(db_column='Uttar Dinajpur', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    purba_medinipur = models.FloatField(db_column='Purba Medinipur', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    haora = models.FloatField(db_column='Haora', blank=True, null=True)  # Field name made lowercase.
    north_twenty_four_parganas = models.FloatField(db_column='North Twenty Four Parganas', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    birbhum = models.FloatField(db_column='Birbhum', blank=True, null=True)  # Field name made lowercase.
    jamtara = models.FloatField(db_column='Jamtara', blank=True, null=True)  # Field name made lowercase.
    saraikela_kharsawan = models.FloatField(db_column='Saraikela-Kharsawan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    simdega = models.FloatField(db_column='Simdega', blank=True, null=True)  # Field name made lowercase.
    latehar = models.FloatField(db_column='Latehar', blank=True, null=True)  # Field name made lowercase.
    khunti = models.FloatField(db_column='Khunti', blank=True, null=True)  # Field name made lowercase.
    pashchimi_singhbhum = models.FloatField(db_column='Pashchimi Singhbhum', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hazaribagh = models.FloatField(db_column='Hazaribagh', blank=True, null=True)  # Field name made lowercase.
    chatra = models.FloatField(db_column='Chatra', blank=True, null=True)  # Field name made lowercase.
    purbi_singhbhum = models.FloatField(db_column='Purbi Singhbhum', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kodarma = models.FloatField(db_column='Kodarma', blank=True, null=True)  # Field name made lowercase.
    giridih = models.FloatField(db_column='Giridih', blank=True, null=True)  # Field name made lowercase.
    bokaro = models.FloatField(db_column='Bokaro', blank=True, null=True)  # Field name made lowercase.
    deoghar = models.FloatField(db_column='Deoghar', blank=True, null=True)  # Field name made lowercase.
    gumla = models.FloatField(db_column='Gumla', blank=True, null=True)  # Field name made lowercase.
    ramgarh = models.FloatField(db_column='Ramgarh', blank=True, null=True)  # Field name made lowercase.
    garhwa = models.FloatField(db_column='Garhwa', blank=True, null=True)  # Field name made lowercase.
    ranchi = models.FloatField(db_column='Ranchi', blank=True, null=True)  # Field name made lowercase.
    pakur = models.FloatField(db_column='Pakur', blank=True, null=True)  # Field name made lowercase.
    gopalganj = models.FloatField(db_column='Gopalganj', blank=True, null=True)  # Field name made lowercase.
    vaishali = models.FloatField(db_column='Vaishali', blank=True, null=True)  # Field name made lowercase.
    siwan = models.FloatField(db_column='Siwan', blank=True, null=True)  # Field name made lowercase.
    sheohar = models.FloatField(db_column='Sheohar', blank=True, null=True)  # Field name made lowercase.
    buxar = models.FloatField(db_column='Buxar', blank=True, null=True)  # Field name made lowercase.
    madhubani = models.FloatField(db_column='Madhubani', blank=True, null=True)  # Field name made lowercase.
    supaul = models.FloatField(db_column='Supaul', blank=True, null=True)  # Field name made lowercase.
    bhojpur = models.FloatField(db_column='Bhojpur', blank=True, null=True)  # Field name made lowercase.
    darbhanga = models.FloatField(db_column='Darbhanga', blank=True, null=True)  # Field name made lowercase.
    samastipur = models.FloatField(db_column='Samastipur', blank=True, null=True)  # Field name made lowercase.
    kaimur_bhabua = models.FloatField(db_column='Kaimur (Bhabua)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rohtas = models.FloatField(db_column='Rohtas', blank=True, null=True)  # Field name made lowercase.
    khagaria = models.FloatField(db_column='Khagaria', blank=True, null=True)  # Field name made lowercase.
    lohardaga = models.FloatField(db_column='Lohardaga', blank=True, null=True)  # Field name made lowercase.
    sahibganj = models.FloatField(db_column='Sahibganj', blank=True, null=True)  # Field name made lowercase.
    godda = models.FloatField(db_column='Godda', blank=True, null=True)  # Field name made lowercase.
    palamu = models.FloatField(db_column='Palamu', blank=True, null=True)  # Field name made lowercase.
    arwal = models.FloatField(db_column='Arwal', blank=True, null=True)  # Field name made lowercase.
    bhagalpur = models.FloatField(db_column='Bhagalpur', blank=True, null=True)  # Field name made lowercase.
    purnia = models.FloatField(db_column='Purnia', blank=True, null=True)  # Field name made lowercase.
    madhepura = models.FloatField(db_column='Madhepura', blank=True, null=True)  # Field name made lowercase.
    munger = models.FloatField(db_column='Munger', blank=True, null=True)  # Field name made lowercase.
    sitamarhi = models.FloatField(db_column='Sitamarhi', blank=True, null=True)  # Field name made lowercase.
    purba_champaran = models.FloatField(db_column='Purba Champaran', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lakhisarai = models.FloatField(db_column='Lakhisarai', blank=True, null=True)  # Field name made lowercase.
    jamui = models.FloatField(db_column='Jamui', blank=True, null=True)  # Field name made lowercase.
    begusarai = models.FloatField(db_column='Begusarai', blank=True, null=True)  # Field name made lowercase.
    nalanda = models.FloatField(db_column='Nalanda', blank=True, null=True)  # Field name made lowercase.
    katihar = models.FloatField(db_column='Katihar', blank=True, null=True)  # Field name made lowercase.
    west = models.FloatField(db_column='West', blank=True, null=True)  # Field name made lowercase.
    mewat = models.FloatField(db_column='Mewat', blank=True, null=True)  # Field name made lowercase.
    jhajjar = models.FloatField(db_column='Jhajjar', blank=True, null=True)  # Field name made lowercase.
    bhiwani = models.FloatField(db_column='Bhiwani', blank=True, null=True)  # Field name made lowercase.
    kaithal = models.FloatField(db_column='Kaithal', blank=True, null=True)  # Field name made lowercase.
    siddharthnagar = models.FloatField(db_column='Siddharthnagar', blank=True, null=True)  # Field name made lowercase.
    sant_kabir_nagar = models.FloatField(db_column='Sant Kabir Nagar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dhanbad = models.FloatField(db_column='Dhanbad', blank=True, null=True)  # Field name made lowercase.
    dumka = models.FloatField(db_column='Dumka', blank=True, null=True)  # Field name made lowercase.
    kishanganj = models.FloatField(db_column='Kishanganj', blank=True, null=True)  # Field name made lowercase.
    gaya = models.FloatField(db_column='Gaya', blank=True, null=True)  # Field name made lowercase.
    banka = models.FloatField(db_column='Banka', blank=True, null=True)  # Field name made lowercase.
    aurangabad = models.FloatField(db_column='Aurangabad', blank=True, null=True)  # Field name made lowercase.
    nawada = models.FloatField(db_column='Nawada', blank=True, null=True)  # Field name made lowercase.
    araria = models.FloatField(db_column='Araria', blank=True, null=True)  # Field name made lowercase.
    pashchim_champaran = models.FloatField(db_column='Pashchim Champaran', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    muzaffarpur = models.FloatField(db_column='Muzaffarpur', blank=True, null=True)  # Field name made lowercase.
    saran = models.FloatField(db_column='Saran', blank=True, null=True)  # Field name made lowercase.
    new_delhi = models.FloatField(db_column='New Delhi', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sonipat = models.FloatField(db_column='Sonipat', blank=True, null=True)  # Field name made lowercase.
    karnal = models.FloatField(db_column='Karnal', blank=True, null=True)  # Field name made lowercase.
    kurukshetra = models.FloatField(db_column='Kurukshetra', blank=True, null=True)  # Field name made lowercase.
    jind = models.FloatField(db_column='Jind', blank=True, null=True)  # Field name made lowercase.
    panipat = models.FloatField(db_column='Panipat', blank=True, null=True)  # Field name made lowercase.
    mahendragarh = models.FloatField(db_column='Mahendragarh', blank=True, null=True)  # Field name made lowercase.
    fatehabad = models.FloatField(db_column='Fatehabad', blank=True, null=True)  # Field name made lowercase.
    shahid_bhagat_singh_nagar = models.FloatField(db_column='Shahid Bhagat Singh Nagar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mandya = models.FloatField(db_column='Mandya', blank=True, null=True)  # Field name made lowercase.
    mysore = models.FloatField(db_column='Mysore', blank=True, null=True)  # Field name made lowercase.
    chikkaballapura = models.FloatField(db_column='Chikkaballapura', blank=True, null=True)  # Field name made lowercase.
    yadgir = models.FloatField(db_column='Yadgir', blank=True, null=True)  # Field name made lowercase.
    chikmagalur = models.FloatField(db_column='Chikmagalur', blank=True, null=True)  # Field name made lowercase.
    chitradurga = models.FloatField(db_column='Chitradurga', blank=True, null=True)  # Field name made lowercase.
    haveri = models.FloatField(db_column='Haveri', blank=True, null=True)  # Field name made lowercase.
    dakshina_kannada = models.FloatField(db_column='Dakshina Kannada', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    raichur = models.FloatField(db_column='Raichur', blank=True, null=True)  # Field name made lowercase.
    kolar = models.FloatField(db_column='Kolar', blank=True, null=True)  # Field name made lowercase.
    bijapur = models.FloatField(db_column='Bijapur', blank=True, null=True)  # Field name made lowercase.
    uttara_kannada = models.FloatField(db_column='Uttara Kannada', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    davanagere = models.FloatField(db_column='Davanagere', blank=True, null=True)  # Field name made lowercase.
    dharwad = models.FloatField(db_column='Dharwad', blank=True, null=True)  # Field name made lowercase.
    bidar = models.FloatField(db_column='Bidar', blank=True, null=True)  # Field name made lowercase.
    chamarajanagar = models.FloatField(db_column='Chamarajanagar', blank=True, null=True)  # Field name made lowercase.
    gulbarga = models.FloatField(db_column='Gulbarga', blank=True, null=True)  # Field name made lowercase.
    gadag = models.FloatField(db_column='Gadag', blank=True, null=True)  # Field name made lowercase.
    udupi = models.FloatField(db_column='Udupi', blank=True, null=True)  # Field name made lowercase.
    bagalkot = models.FloatField(db_column='Bagalkot', blank=True, null=True)  # Field name made lowercase.
    hassan = models.FloatField(db_column='Hassan', blank=True, null=True)  # Field name made lowercase.
    shimoga = models.FloatField(db_column='Shimoga', blank=True, null=True)  # Field name made lowercase.
    bellary = models.FloatField(db_column='Bellary', blank=True, null=True)  # Field name made lowercase.
    kodagu = models.FloatField(db_column='Kodagu', blank=True, null=True)  # Field name made lowercase.
    east = models.FloatField(db_column='East', blank=True, null=True)  # Field name made lowercase.
    south = models.FloatField(db_column='South', blank=True, null=True)  # Field name made lowercase.
    north_west = models.FloatField(db_column='North West', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    south_west = models.FloatField(db_column='South West', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    faridabad = models.FloatField(db_column='Faridabad', blank=True, null=True)  # Field name made lowercase.
    sirsa = models.FloatField(db_column='Sirsa', blank=True, null=True)  # Field name made lowercase.
    hisar = models.FloatField(db_column='Hisar', blank=True, null=True)  # Field name made lowercase.
    bangalore_rural = models.FloatField(db_column='Bangalore Rural', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tumkur = models.FloatField(db_column='Tumkur', blank=True, null=True)  # Field name made lowercase.
    belgaum = models.FloatField(db_column='Belgaum', blank=True, null=True)  # Field name made lowercase.
    koppal = models.FloatField(db_column='Koppal', blank=True, null=True)  # Field name made lowercase.
    bangalore = models.FloatField(db_column='Bangalore', blank=True, null=True)  # Field name made lowercase.
    ramanagara = models.FloatField(db_column='Ramanagara', blank=True, null=True)  # Field name made lowercase.
    washim = models.FloatField(db_column='Washim', blank=True, null=True)  # Field name made lowercase.
    ahmadnagar = models.FloatField(db_column='Ahmadnagar', blank=True, null=True)  # Field name made lowercase.
    latur = models.FloatField(db_column='Latur', blank=True, null=True)  # Field name made lowercase.
    solapur = models.FloatField(db_column='Solapur', blank=True, null=True)  # Field name made lowercase.
    nashik = models.FloatField(db_column='Nashik', blank=True, null=True)  # Field name made lowercase.
    osmanabad = models.FloatField(db_column='Osmanabad', blank=True, null=True)  # Field name made lowercase.
    sindhudurg = models.FloatField(db_column='Sindhudurg', blank=True, null=True)  # Field name made lowercase.
    kolhapur = models.FloatField(db_column='Kolhapur', blank=True, null=True)  # Field name made lowercase.
    chandrapur = models.FloatField(db_column='Chandrapur', blank=True, null=True)  # Field name made lowercase.
    akola = models.FloatField(db_column='Akola', blank=True, null=True)  # Field name made lowercase.
    parbhani = models.FloatField(db_column='Parbhani', blank=True, null=True)  # Field name made lowercase.
    yavatmal = models.FloatField(db_column='Yavatmal', blank=True, null=True)  # Field name made lowercase.
    nanded = models.FloatField(db_column='Nanded', blank=True, null=True)  # Field name made lowercase.
    dhule = models.FloatField(db_column='Dhule', blank=True, null=True)  # Field name made lowercase.
    satara = models.FloatField(db_column='Satara', blank=True, null=True)  # Field name made lowercase.
    sangli = models.FloatField(db_column='Sangli', blank=True, null=True)  # Field name made lowercase.
    hingoli = models.FloatField(db_column='Hingoli', blank=True, null=True)  # Field name made lowercase.
    pune = models.FloatField(db_column='Pune', blank=True, null=True)  # Field name made lowercase.
    central = models.FloatField(db_column='Central', blank=True, null=True)  # Field name made lowercase.
    rewari = models.FloatField(db_column='Rewari', blank=True, null=True)  # Field name made lowercase.
    rohtak = models.FloatField(db_column='Rohtak', blank=True, null=True)  # Field name made lowercase.
    ambala = models.FloatField(db_column='Ambala', blank=True, null=True)  # Field name made lowercase.
    chandigarh = models.FloatField(db_column='Chandigarh', blank=True, null=True)  # Field name made lowercase.
    gondiya = models.FloatField(db_column='Gondiya', blank=True, null=True)  # Field name made lowercase.
    amravati = models.FloatField(db_column='Amravati', blank=True, null=True)  # Field name made lowercase.
    nandurbar = models.FloatField(db_column='Nandurbar', blank=True, null=True)  # Field name made lowercase.
    ratnagiri = models.FloatField(db_column='Ratnagiri', blank=True, null=True)  # Field name made lowercase.
    wardha = models.FloatField(db_column='Wardha', blank=True, null=True)  # Field name made lowercase.
    aurangabad_1 = models.FloatField(db_column='Aurangabad.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    buldana = models.FloatField(db_column='Buldana', blank=True, null=True)  # Field name made lowercase.
    gadchiroli = models.FloatField(db_column='Gadchiroli', blank=True, null=True)  # Field name made lowercase.
    jalgaon = models.FloatField(db_column='Jalgaon', blank=True, null=True)  # Field name made lowercase.
    raigarh = models.FloatField(db_column='Raigarh', blank=True, null=True)  # Field name made lowercase.
    bhandara = models.FloatField(db_column='Bhandara', blank=True, null=True)  # Field name made lowercase.
    bid = models.FloatField(db_column='Bid', blank=True, null=True)  # Field name made lowercase.
    jalna = models.FloatField(db_column='Jalna', blank=True, null=True)  # Field name made lowercase.
    thane = models.FloatField(db_column='Thane', blank=True, null=True)  # Field name made lowercase.
    palghar = models.FloatField(db_column='Palghar', blank=True, null=True)  # Field name made lowercase.
    varanasi = models.FloatField(db_column='Varanasi', blank=True, null=True)  # Field name made lowercase.
    north_east = models.FloatField(db_column='North East', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patiala = models.FloatField(db_column='Patiala', blank=True, null=True)  # Field name made lowercase.
    tarn_taran = models.FloatField(db_column='Tarn Taran', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kapurthala = models.FloatField(db_column='Kapurthala', blank=True, null=True)  # Field name made lowercase.
    fatehgarh_sahib = models.FloatField(db_column='Fatehgarh Sahib', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sangrur = models.FloatField(db_column='Sangrur', blank=True, null=True)  # Field name made lowercase.
    yanam = models.FloatField(db_column='Yanam', blank=True, null=True)  # Field name made lowercase.
    tamenglong = models.FloatField(db_column='Tamenglong', blank=True, null=True)  # Field name made lowercase.
    bara_banki = models.FloatField(db_column='Bara Banki', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mahoba = models.FloatField(db_column='Mahoba', blank=True, null=True)  # Field name made lowercase.
    mahrajganj = models.FloatField(db_column='Mahrajganj', blank=True, null=True)  # Field name made lowercase.
    mirzapur = models.FloatField(db_column='Mirzapur', blank=True, null=True)  # Field name made lowercase.
    kushinagar = models.FloatField(db_column='Kushinagar', blank=True, null=True)  # Field name made lowercase.
    north = models.FloatField(db_column='North', blank=True, null=True)  # Field name made lowercase.
    gurgaon = models.FloatField(db_column='Gurgaon', blank=True, null=True)  # Field name made lowercase.
    yamunanagar = models.FloatField(db_column='Yamunanagar', blank=True, null=True)  # Field name made lowercase.
    palwal = models.FloatField(db_column='Palwal', blank=True, null=True)  # Field name made lowercase.
    panchkula = models.FloatField(db_column='Panchkula', blank=True, null=True)  # Field name made lowercase.
    mamit = models.FloatField(db_column='Mamit', blank=True, null=True)  # Field name made lowercase.
    chandel = models.FloatField(db_column='Chandel', blank=True, null=True)  # Field name made lowercase.
    deoria = models.FloatField(db_column='Deoria', blank=True, null=True)  # Field name made lowercase.
    unnao = models.FloatField(db_column='Unnao', blank=True, null=True)  # Field name made lowercase.
    fatehpur = models.FloatField(db_column='Fatehpur', blank=True, null=True)  # Field name made lowercase.
    mau = models.FloatField(db_column='Mau', blank=True, null=True)  # Field name made lowercase.
    rae_bareli = models.FloatField(db_column='Rae Bareli', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amethi = models.FloatField(db_column='Amethi', blank=True, null=True)  # Field name made lowercase.
    ghaziabad = models.FloatField(db_column='Ghaziabad', blank=True, null=True)  # Field name made lowercase.
    muzaffarnagar = models.FloatField(db_column='Muzaffarnagar', blank=True, null=True)  # Field name made lowercase.
    gautam_buddha_nagar = models.FloatField(db_column='Gautam Buddha Nagar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    saharanpur = models.FloatField(db_column='Saharanpur', blank=True, null=True)  # Field name made lowercase.
    etawah = models.FloatField(db_column='Etawah', blank=True, null=True)  # Field name made lowercase.
    agra = models.FloatField(db_column='Agra', blank=True, null=True)  # Field name made lowercase.
    cuddalore = models.FloatField(db_column='Cuddalore', blank=True, null=True)  # Field name made lowercase.
    pathankot = models.FloatField(db_column='Pathankot', blank=True, null=True)  # Field name made lowercase.
    gurdaspur = models.FloatField(db_column='Gurdaspur', blank=True, null=True)  # Field name made lowercase.
    mansa = models.FloatField(db_column='Mansa', blank=True, null=True)  # Field name made lowercase.
    amritsar = models.FloatField(db_column='Amritsar', blank=True, null=True)  # Field name made lowercase.
    kohima = models.FloatField(db_column='Kohima', blank=True, null=True)  # Field name made lowercase.
    wokha = models.FloatField(db_column='Wokha', blank=True, null=True)  # Field name made lowercase.
    zunheboto = models.FloatField(db_column='Zunheboto', blank=True, null=True)  # Field name made lowercase.
    kiphire = models.FloatField(db_column='Kiphire', blank=True, null=True)  # Field name made lowercase.
    faridkot = models.FloatField(db_column='Faridkot', blank=True, null=True)  # Field name made lowercase.
    ludhiana = models.FloatField(db_column='Ludhiana', blank=True, null=True)  # Field name made lowercase.
    bathinda = models.FloatField(db_column='Bathinda', blank=True, null=True)  # Field name made lowercase.
    jalandhar = models.FloatField(db_column='Jalandhar', blank=True, null=True)  # Field name made lowercase.
    moga = models.FloatField(db_column='Moga', blank=True, null=True)  # Field name made lowercase.
    hoshiarpur = models.FloatField(db_column='Hoshiarpur', blank=True, null=True)  # Field name made lowercase.
    dimapur = models.FloatField(db_column='Dimapur', blank=True, null=True)  # Field name made lowercase.
    peren = models.FloatField(db_column='Peren', blank=True, null=True)  # Field name made lowercase.
    lohit = models.FloatField(db_column='Lohit', blank=True, null=True)  # Field name made lowercase.
    west_siang = models.FloatField(db_column='West Siang', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    upper_subansiri = models.FloatField(db_column='Upper Subansiri', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    changlang = models.FloatField(db_column='Changlang', blank=True, null=True)  # Field name made lowercase.
    tirap = models.FloatField(db_column='Tirap', blank=True, null=True)  # Field name made lowercase.
    lower_subansiri = models.FloatField(db_column='Lower Subansiri', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    east_kameng = models.FloatField(db_column='East Kameng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    upper_siang = models.FloatField(db_column='Upper Siang', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anjaw = models.FloatField(db_column='Anjaw', blank=True, null=True)  # Field name made lowercase.
    east_siang = models.FloatField(db_column='East Siang', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dibang_valley = models.FloatField(db_column='Dibang Valley', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kurung_kumey = models.FloatField(db_column='Kurung Kumey', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    west_kameng = models.FloatField(db_column='West Kameng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lower_dibang_valley = models.FloatField(db_column='Lower Dibang Valley', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tawang = models.FloatField(db_column='Tawang', blank=True, null=True)  # Field name made lowercase.
    papum_pare = models.FloatField(db_column='Papum Pare', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    goalpara = models.FloatField(db_column='Goalpara', blank=True, null=True)  # Field name made lowercase.
    baksa = models.FloatField(db_column='Baksa', blank=True, null=True)  # Field name made lowercase.
    nagaon = models.FloatField(db_column='Nagaon', blank=True, null=True)  # Field name made lowercase.
    pudukkottai = models.FloatField(db_column='Pudukkottai', blank=True, null=True)  # Field name made lowercase.
    vellore = models.FloatField(db_column='Vellore', blank=True, null=True)  # Field name made lowercase.
    chandauli = models.FloatField(db_column='Chandauli', blank=True, null=True)  # Field name made lowercase.
    muktsar = models.FloatField(db_column='Muktsar', blank=True, null=True)  # Field name made lowercase.
    rupnagar = models.FloatField(db_column='Rupnagar', blank=True, null=True)  # Field name made lowercase.
    firozpur = models.FloatField(db_column='Firozpur', blank=True, null=True)  # Field name made lowercase.
    fazilka = models.FloatField(db_column='Fazilka', blank=True, null=True)  # Field name made lowercase.
    west_tripura = models.FloatField(db_column='West Tripura', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    barnala = models.FloatField(db_column='Barnala', blank=True, null=True)  # Field name made lowercase.
    sahibzada_ajit_singh_nagar = models.FloatField(db_column='Sahibzada Ajit Singh Nagar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mumbai = models.FloatField(db_column='Mumbai', blank=True, null=True)  # Field name made lowercase.
    lunglei = models.FloatField(db_column='Lunglei', blank=True, null=True)  # Field name made lowercase.
    kolasib = models.FloatField(db_column='Kolasib', blank=True, null=True)  # Field name made lowercase.
    lawngtlai = models.FloatField(db_column='Lawngtlai', blank=True, null=True)  # Field name made lowercase.
    saiha = models.FloatField(db_column='Saiha', blank=True, null=True)  # Field name made lowercase.
    champhai = models.FloatField(db_column='Champhai', blank=True, null=True)  # Field name made lowercase.
    dhalai = models.FloatField(db_column='Dhalai', blank=True, null=True)  # Field name made lowercase.
    unokoti = models.FloatField(db_column='Unokoti', blank=True, null=True)  # Field name made lowercase.
    north_tripura = models.FloatField(db_column='North Tripura', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gomati = models.FloatField(db_column='Gomati', blank=True, null=True)  # Field name made lowercase.
    south_tripura = models.FloatField(db_column='South Tripura', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    south_garo_hills = models.FloatField(db_column='South Garo Hills', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ribhoi = models.FloatField(db_column='Ribhoi', blank=True, null=True)  # Field name made lowercase.
    east_khasi_hills = models.FloatField(db_column='East Khasi Hills', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    west_khasi_hills = models.FloatField(db_column='West Khasi Hills', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    south_west_khasi_hills = models.FloatField(db_column='South West Khasi Hills', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    west_garo_hills = models.FloatField(db_column='West Garo Hills', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jhansi = models.FloatField(db_column='Jhansi', blank=True, null=True)  # Field name made lowercase.
    banda = models.FloatField(db_column='Banda', blank=True, null=True)  # Field name made lowercase.
    sonbhadra = models.FloatField(db_column='Sonbhadra', blank=True, null=True)  # Field name made lowercase.
    lalitpur = models.FloatField(db_column='Lalitpur', blank=True, null=True)  # Field name made lowercase.
    ghazipur = models.FloatField(db_column='Ghazipur', blank=True, null=True)  # Field name made lowercase.
    krishnagiri = models.FloatField(db_column='Krishnagiri', blank=True, null=True)  # Field name made lowercase.
    erode = models.FloatField(db_column='Erode', blank=True, null=True)  # Field name made lowercase.
    coimbatore = models.FloatField(db_column='Coimbatore', blank=True, null=True)  # Field name made lowercase.
    warangal_r = models.FloatField(db_column='Warangal (R)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    serchhip = models.FloatField(db_column='Serchhip', blank=True, null=True)  # Field name made lowercase.
    aizawl = models.FloatField(db_column='Aizawl', blank=True, null=True)  # Field name made lowercase.
    mumbai_suburban = models.FloatField(db_column='Mumbai Suburban', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nagpur = models.FloatField(db_column='Nagpur', blank=True, null=True)  # Field name made lowercase.
    north_goa = models.FloatField(db_column='North Goa', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    south_goa = models.FloatField(db_column='South Goa', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    north_middle_andaman = models.FloatField(db_column='North  & Middle Andaman', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    south_andaman = models.FloatField(db_column='South Andaman', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nicobars = models.FloatField(db_column='Nicobars', blank=True, null=True)  # Field name made lowercase.
    anugul = models.FloatField(db_column='Anugul', blank=True, null=True)  # Field name made lowercase.
    karaikal = models.FloatField(db_column='Karaikal', blank=True, null=True)  # Field name made lowercase.
    puducherry = models.FloatField(db_column='Puducherry', blank=True, null=True)  # Field name made lowercase.
    mahe = models.FloatField(db_column='Mahe', blank=True, null=True)  # Field name made lowercase.
    ukhrul = models.FloatField(db_column='Ukhrul', blank=True, null=True)  # Field name made lowercase.
    bishnupur = models.FloatField(db_column='Bishnupur', blank=True, null=True)  # Field name made lowercase.
    churachandpur = models.FloatField(db_column='Churachandpur', blank=True, null=True)  # Field name made lowercase.
    thoubal = models.FloatField(db_column='Thoubal', blank=True, null=True)  # Field name made lowercase.
    imphal_east = models.FloatField(db_column='Imphal East', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    senapati = models.FloatField(db_column='Senapati', blank=True, null=True)  # Field name made lowercase.
    imphal_west = models.FloatField(db_column='Imphal West', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mon = models.FloatField(db_column='Mon', blank=True, null=True)  # Field name made lowercase.
    tuensang = models.FloatField(db_column='Tuensang', blank=True, null=True)  # Field name made lowercase.
    mokokchung = models.FloatField(db_column='Mokokchung', blank=True, null=True)  # Field name made lowercase.
    longleng = models.FloatField(db_column='Longleng', blank=True, null=True)  # Field name made lowercase.
    phek = models.FloatField(db_column='Phek', blank=True, null=True)  # Field name made lowercase.
    nalbari = models.FloatField(db_column='Nalbari', blank=True, null=True)  # Field name made lowercase.
    dhubri = models.FloatField(db_column='Dhubri', blank=True, null=True)  # Field name made lowercase.
    sivasagar = models.FloatField(db_column='Sivasagar', blank=True, null=True)  # Field name made lowercase.
    karimganj = models.FloatField(db_column='Karimganj', blank=True, null=True)  # Field name made lowercase.
    tinsukia = models.FloatField(db_column='Tinsukia', blank=True, null=True)  # Field name made lowercase.
    koraput = models.FloatField(db_column='Koraput', blank=True, null=True)  # Field name made lowercase.
    hailakandi = models.FloatField(db_column='Hailakandi', blank=True, null=True)  # Field name made lowercase.
    nabarangapur = models.FloatField(db_column='Nabarangapur', blank=True, null=True)  # Field name made lowercase.
    bargarh = models.FloatField(db_column='Bargarh', blank=True, null=True)  # Field name made lowercase.
    chirang = models.FloatField(db_column='Chirang', blank=True, null=True)  # Field name made lowercase.
    cachar = models.FloatField(db_column='Cachar', blank=True, null=True)  # Field name made lowercase.
    darrang = models.FloatField(db_column='Darrang', blank=True, null=True)  # Field name made lowercase.
    kamrup = models.FloatField(db_column='Kamrup', blank=True, null=True)  # Field name made lowercase.
    dibrugarh = models.FloatField(db_column='Dibrugarh', blank=True, null=True)  # Field name made lowercase.
    barpeta = models.FloatField(db_column='Barpeta', blank=True, null=True)  # Field name made lowercase.
    balangir = models.FloatField(db_column='Balangir', blank=True, null=True)  # Field name made lowercase.
    dhemaji = models.FloatField(db_column='Dhemaji', blank=True, null=True)  # Field name made lowercase.
    sonitpur = models.FloatField(db_column='Sonitpur', blank=True, null=True)  # Field name made lowercase.
    udalguri = models.FloatField(db_column='Udalguri', blank=True, null=True)  # Field name made lowercase.
    jhunjhunun = models.FloatField(db_column='Jhunjhunun', blank=True, null=True)  # Field name made lowercase.
    jaisalmer = models.FloatField(db_column='Jaisalmer', blank=True, null=True)  # Field name made lowercase.
    sikar = models.FloatField(db_column='Sikar', blank=True, null=True)  # Field name made lowercase.
    hanumangarh = models.FloatField(db_column='Hanumangarh', blank=True, null=True)  # Field name made lowercase.
    nagaur = models.FloatField(db_column='Nagaur', blank=True, null=True)  # Field name made lowercase.
    barmer = models.FloatField(db_column='Barmer', blank=True, null=True)  # Field name made lowercase.
    ganganagar = models.FloatField(db_column='Ganganagar', blank=True, null=True)  # Field name made lowercase.
    jodhpur = models.FloatField(db_column='Jodhpur', blank=True, null=True)  # Field name made lowercase.
    churu = models.FloatField(db_column='Churu', blank=True, null=True)  # Field name made lowercase.
    bikaner = models.FloatField(db_column='Bikaner', blank=True, null=True)  # Field name made lowercase.
    pratapgarh = models.FloatField(db_column='Pratapgarh', blank=True, null=True)  # Field name made lowercase.
    morigaon = models.FloatField(db_column='Morigaon', blank=True, null=True)  # Field name made lowercase.
    karbi_anglong = models.FloatField(db_column='Karbi Anglong', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lakhimpur = models.FloatField(db_column='Lakhimpur', blank=True, null=True)  # Field name made lowercase.
    golaghat = models.FloatField(db_column='Golaghat', blank=True, null=True)  # Field name made lowercase.
    dima_hasao = models.FloatField(db_column='Dima Hasao', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pali = models.FloatField(db_column='Pali', blank=True, null=True)  # Field name made lowercase.
    rajsamand = models.FloatField(db_column='Rajsamand', blank=True, null=True)  # Field name made lowercase.
    ajmer = models.FloatField(db_column='Ajmer', blank=True, null=True)  # Field name made lowercase.
    bharatpur = models.FloatField(db_column='Bharatpur', blank=True, null=True)  # Field name made lowercase.
    dungarpur = models.FloatField(db_column='Dungarpur', blank=True, null=True)  # Field name made lowercase.
    chittaurgarh = models.FloatField(db_column='Chittaurgarh', blank=True, null=True)  # Field name made lowercase.
    udaipur = models.FloatField(db_column='Udaipur', blank=True, null=True)  # Field name made lowercase.
    jalor = models.FloatField(db_column='Jalor', blank=True, null=True)  # Field name made lowercase.
    dausa = models.FloatField(db_column='Dausa', blank=True, null=True)  # Field name made lowercase.
    sirohi = models.FloatField(db_column='Sirohi', blank=True, null=True)  # Field name made lowercase.
    bongaigaon = models.FloatField(db_column='Bongaigaon', blank=True, null=True)  # Field name made lowercase.
    west_jaintia_hills = models.FloatField(db_column='West Jaintia Hills', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sivaganga = models.FloatField(db_column='Sivaganga', blank=True, null=True)  # Field name made lowercase.
    thanjavur = models.FloatField(db_column='Thanjavur', blank=True, null=True)  # Field name made lowercase.
    tiruvannamalai = models.FloatField(db_column='Tiruvannamalai', blank=True, null=True)  # Field name made lowercase.
    kamrup_metropolitan = models.FloatField(db_column='Kamrup Metropolitan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ramanathapuram = models.FloatField(db_column='Ramanathapuram', blank=True, null=True)  # Field name made lowercase.
    tirunelveli = models.FloatField(db_column='Tirunelveli', blank=True, null=True)  # Field name made lowercase.
    virudhunagar = models.FloatField(db_column='Virudhunagar', blank=True, null=True)  # Field name made lowercase.
    kokrajhar = models.FloatField(db_column='Kokrajhar', blank=True, null=True)  # Field name made lowercase.
    jorhat = models.FloatField(db_column='Jorhat', blank=True, null=True)  # Field name made lowercase.
    khowai = models.FloatField(db_column='Khowai', blank=True, null=True)  # Field name made lowercase.
    sipahijula = models.FloatField(db_column='Sipahijula', blank=True, null=True)  # Field name made lowercase.
    east_garo_hills = models.FloatField(db_column='East Garo Hills', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    north_garo_hills = models.FloatField(db_column='North Garo Hills', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subarnapur = models.FloatField(db_column='Subarnapur', blank=True, null=True)  # Field name made lowercase.
    puri = models.FloatField(db_column='Puri', blank=True, null=True)  # Field name made lowercase.
    debagarh = models.FloatField(db_column='Debagarh', blank=True, null=True)  # Field name made lowercase.
    south_west_garo_hills = models.FloatField(db_column='South West Garo Hills', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    east_jaintia_hills = models.FloatField(db_column='East Jaintia Hills', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jagatsinghapur = models.FloatField(db_column='Jagatsinghapur', blank=True, null=True)  # Field name made lowercase.
    kandhamal = models.FloatField(db_column='Kandhamal', blank=True, null=True)  # Field name made lowercase.
    khordha = models.FloatField(db_column='Khordha', blank=True, null=True)  # Field name made lowercase.
    mayurbhanj = models.FloatField(db_column='Mayurbhanj', blank=True, null=True)  # Field name made lowercase.
    malkangiri = models.FloatField(db_column='Malkangiri', blank=True, null=True)  # Field name made lowercase.
    baleshwar = models.FloatField(db_column='Baleshwar', blank=True, null=True)  # Field name made lowercase.
    sambalpur = models.FloatField(db_column='Sambalpur', blank=True, null=True)  # Field name made lowercase.
    gajapati = models.FloatField(db_column='Gajapati', blank=True, null=True)  # Field name made lowercase.
    dhenkanal = models.FloatField(db_column='Dhenkanal', blank=True, null=True)  # Field name made lowercase.
    nayagarh = models.FloatField(db_column='Nayagarh', blank=True, null=True)  # Field name made lowercase.
    cuttack = models.FloatField(db_column='Cuttack', blank=True, null=True)  # Field name made lowercase.
    jajapur = models.FloatField(db_column='Jajapur', blank=True, null=True)  # Field name made lowercase.
    kalahandi = models.FloatField(db_column='Kalahandi', blank=True, null=True)  # Field name made lowercase.
    baudh = models.FloatField(db_column='Baudh', blank=True, null=True)  # Field name made lowercase.
    kendrapara = models.FloatField(db_column='Kendrapara', blank=True, null=True)  # Field name made lowercase.
    kendujhar = models.FloatField(db_column='Kendujhar', blank=True, null=True)  # Field name made lowercase.
    ganjam = models.FloatField(db_column='Ganjam', blank=True, null=True)  # Field name made lowercase.
    sundargarh = models.FloatField(db_column='Sundargarh', blank=True, null=True)  # Field name made lowercase.
    bhadrak = models.FloatField(db_column='Bhadrak', blank=True, null=True)  # Field name made lowercase.
    nuapada = models.FloatField(db_column='Nuapada', blank=True, null=True)  # Field name made lowercase.
    rayagada = models.FloatField(db_column='Rayagada', blank=True, null=True)  # Field name made lowercase.
    jharsuguda = models.FloatField(db_column='Jharsuguda', blank=True, null=True)  # Field name made lowercase.
    bemetra = models.FloatField(db_column='Bemetra', blank=True, null=True)  # Field name made lowercase.
    bastar = models.FloatField(db_column='Bastar', blank=True, null=True)  # Field name made lowercase.
    thiruvarur = models.FloatField(db_column='Thiruvarur', blank=True, null=True)  # Field name made lowercase.
    thiruvallur = models.FloatField(db_column='Thiruvallur', blank=True, null=True)  # Field name made lowercase.
    mungeli = models.FloatField(db_column='Mungeli', blank=True, null=True)  # Field name made lowercase.
    bilaspur_1 = models.FloatField(db_column='Bilaspur.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gariaband = models.FloatField(db_column='Gariaband', blank=True, null=True)  # Field name made lowercase.
    kabeerdham = models.FloatField(db_column='Kabeerdham', blank=True, null=True)  # Field name made lowercase.
    sukma = models.FloatField(db_column='Sukma', blank=True, null=True)  # Field name made lowercase.
    uttar_bastar_kanker = models.FloatField(db_column='Uttar Bastar Kanker', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    baloda_bazar = models.FloatField(db_column='Baloda Bazar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    balod = models.FloatField(db_column='Balod', blank=True, null=True)  # Field name made lowercase.
    tiruchirappalli = models.FloatField(db_column='Tiruchirappalli', blank=True, null=True)  # Field name made lowercase.
    tiruppur = models.FloatField(db_column='Tiruppur', blank=True, null=True)  # Field name made lowercase.
    madurai = models.FloatField(db_column='Madurai', blank=True, null=True)  # Field name made lowercase.
    karur = models.FloatField(db_column='Karur', blank=True, null=True)  # Field name made lowercase.
    dharmapuri = models.FloatField(db_column='Dharmapuri', blank=True, null=True)  # Field name made lowercase.
    namakkal = models.FloatField(db_column='Namakkal', blank=True, null=True)  # Field name made lowercase.
    moradabad = models.FloatField(db_column='Moradabad', blank=True, null=True)  # Field name made lowercase.
    sambhal = models.FloatField(db_column='Sambhal', blank=True, null=True)  # Field name made lowercase.
    budaun = models.FloatField(db_column='Budaun', blank=True, null=True)  # Field name made lowercase.
    kanshiram_nagar = models.FloatField(db_column='Kanshiram Nagar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bahraich = models.FloatField(db_column='Bahraich', blank=True, null=True)  # Field name made lowercase.
    hapur = models.FloatField(db_column='Hapur', blank=True, null=True)  # Field name made lowercase.
    sitapur = models.FloatField(db_column='Sitapur', blank=True, null=True)  # Field name made lowercase.
    samli = models.FloatField(db_column='Samli', blank=True, null=True)  # Field name made lowercase.
    dakshin_bastar_dantewada = models.FloatField(db_column='Dakshin Bastar Dantewada', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    surguja = models.FloatField(db_column='Surguja', blank=True, null=True)  # Field name made lowercase.
    balrampur = models.FloatField(db_column='Balrampur', blank=True, null=True)  # Field name made lowercase.
    kondagaon = models.FloatField(db_column='Kondagaon', blank=True, null=True)  # Field name made lowercase.
    shrawasti = models.FloatField(db_column='Shrawasti', blank=True, null=True)  # Field name made lowercase.
    narayanpur = models.FloatField(db_column='Narayanpur', blank=True, null=True)  # Field name made lowercase.
    durg = models.FloatField(db_column='Durg', blank=True, null=True)  # Field name made lowercase.
    surajpur = models.FloatField(db_column='Surajpur', blank=True, null=True)  # Field name made lowercase.
    bijapur_1 = models.FloatField(db_column='Bijapur.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mathura = models.FloatField(db_column='Mathura', blank=True, null=True)  # Field name made lowercase.
    etah = models.FloatField(db_column='Etah', blank=True, null=True)  # Field name made lowercase.
    hardoi = models.FloatField(db_column='Hardoi', blank=True, null=True)  # Field name made lowercase.
    balrampur_1 = models.FloatField(db_column='Balrampur.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mahamaya_nagar = models.FloatField(db_column='Mahamaya Nagar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shahjahanpur = models.FloatField(db_column='Shahjahanpur', blank=True, null=True)  # Field name made lowercase.
    farrukhabad = models.FloatField(db_column='Farrukhabad', blank=True, null=True)  # Field name made lowercase.
    kannauj = models.FloatField(db_column='Kannauj', blank=True, null=True)  # Field name made lowercase.
    pilibhit = models.FloatField(db_column='Pilibhit', blank=True, null=True)  # Field name made lowercase.
    mainpuri = models.FloatField(db_column='Mainpuri', blank=True, null=True)  # Field name made lowercase.
    jyotiba_phule_nagar = models.FloatField(db_column='Jyotiba Phule Nagar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    raipur = models.FloatField(db_column='Raipur', blank=True, null=True)  # Field name made lowercase.
    koriya = models.FloatField(db_column='Koriya', blank=True, null=True)  # Field name made lowercase.
    dhamtari = models.FloatField(db_column='Dhamtari', blank=True, null=True)  # Field name made lowercase.
    korba = models.FloatField(db_column='Korba', blank=True, null=True)  # Field name made lowercase.
    raigarh_1 = models.FloatField(db_column='Raigarh.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jashpur = models.FloatField(db_column='Jashpur', blank=True, null=True)  # Field name made lowercase.
    mahasamund = models.FloatField(db_column='Mahasamund', blank=True, null=True)  # Field name made lowercase.
    rajnandgaon = models.FloatField(db_column='Rajnandgaon', blank=True, null=True)  # Field name made lowercase.
    janjgir_champa = models.FloatField(db_column='Janjgir-Champa', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bhilwara = models.FloatField(db_column='Bhilwara', blank=True, null=True)  # Field name made lowercase.
    tonk = models.FloatField(db_column='Tonk', blank=True, null=True)  # Field name made lowercase.
    bundi = models.FloatField(db_column='Bundi', blank=True, null=True)  # Field name made lowercase.
    jaipur = models.FloatField(db_column='Jaipur', blank=True, null=True)  # Field name made lowercase.
    kota = models.FloatField(db_column='Kota', blank=True, null=True)  # Field name made lowercase.
    ariyalur = models.FloatField(db_column='Ariyalur', blank=True, null=True)  # Field name made lowercase.
    theni = models.FloatField(db_column='Theni', blank=True, null=True)  # Field name made lowercase.
    salem = models.FloatField(db_column='Salem', blank=True, null=True)  # Field name made lowercase.
    firozabad = models.FloatField(db_column='Firozabad', blank=True, null=True)  # Field name made lowercase.
    sultanpur = models.FloatField(db_column='Sultanpur', blank=True, null=True)  # Field name made lowercase.
    chitrakoot = models.FloatField(db_column='Chitrakoot', blank=True, null=True)  # Field name made lowercase.
    basti = models.FloatField(db_column='Basti', blank=True, null=True)  # Field name made lowercase.
    gorakhpur = models.FloatField(db_column='Gorakhpur', blank=True, null=True)  # Field name made lowercase.
    lucknow = models.FloatField(db_column='Lucknow', blank=True, null=True)  # Field name made lowercase.
    azamgarh = models.FloatField(db_column='Azamgarh', blank=True, null=True)  # Field name made lowercase.
    faizabad = models.FloatField(db_column='Faizabad', blank=True, null=True)  # Field name made lowercase.
    perambalur = models.FloatField(db_column='Perambalur', blank=True, null=True)  # Field name made lowercase.
    dindigul = models.FloatField(db_column='Dindigul', blank=True, null=True)  # Field name made lowercase.
    meerut = models.FloatField(db_column='Meerut', blank=True, null=True)  # Field name made lowercase.
    aligarh = models.FloatField(db_column='Aligarh', blank=True, null=True)  # Field name made lowercase.
    bulandshahr = models.FloatField(db_column='Bulandshahr', blank=True, null=True)  # Field name made lowercase.
    bijnor = models.FloatField(db_column='Bijnor', blank=True, null=True)  # Field name made lowercase.
    baghpat = models.FloatField(db_column='Baghpat', blank=True, null=True)  # Field name made lowercase.
    kheri = models.FloatField(db_column='Kheri', blank=True, null=True)  # Field name made lowercase.
    rampur = models.FloatField(db_column='Rampur', blank=True, null=True)  # Field name made lowercase.
    bareilly = models.FloatField(db_column='Bareilly', blank=True, null=True)  # Field name made lowercase.
    kaushambi = models.FloatField(db_column='Kaushambi', blank=True, null=True)  # Field name made lowercase.
    jalaun = models.FloatField(db_column='Jalaun', blank=True, null=True)  # Field name made lowercase.
    auraiya = models.FloatField(db_column='Auraiya', blank=True, null=True)  # Field name made lowercase.
    pratapgarh_1 = models.FloatField(db_column='Pratapgarh.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hamirpur_1 = models.FloatField(db_column='Hamirpur.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gonda = models.FloatField(db_column='Gonda', blank=True, null=True)  # Field name made lowercase.
    kanpur_dehat = models.FloatField(db_column='Kanpur Dehat', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jaunpur = models.FloatField(db_column='Jaunpur', blank=True, null=True)  # Field name made lowercase.
    chennai = models.FloatField(db_column='Chennai', blank=True, null=True)  # Field name made lowercase.
    nagapattinam = models.FloatField(db_column='Nagapattinam', blank=True, null=True)  # Field name made lowercase.
    viluppuram = models.FloatField(db_column='Viluppuram', blank=True, null=True)  # Field name made lowercase.
    kancheepuram = models.FloatField(db_column='Kancheepuram', blank=True, null=True)  # Field name made lowercase.
    banswara = models.FloatField(db_column='Banswara', blank=True, null=True)  # Field name made lowercase.
    kanniyakumari = models.FloatField(db_column='Kanniyakumari', blank=True, null=True)  # Field name made lowercase.
    thoothukkudi = models.FloatField(db_column='Thoothukkudi', blank=True, null=True)  # Field name made lowercase.
    allahabad = models.FloatField(db_column='Allahabad', blank=True, null=True)  # Field name made lowercase.
    the_nilgiris = models.FloatField(db_column='The Nilgiris', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jhalawar = models.FloatField(db_column='Jhalawar', blank=True, null=True)  # Field name made lowercase.
    alwar = models.FloatField(db_column='Alwar', blank=True, null=True)  # Field name made lowercase.
    baran = models.FloatField(db_column='Baran', blank=True, null=True)  # Field name made lowercase.
    karauli = models.FloatField(db_column='Karauli', blank=True, null=True)  # Field name made lowercase.
    dhaulpur = models.FloatField(db_column='Dhaulpur', blank=True, null=True)  # Field name made lowercase.
    sawai_madhopur = models.FloatField(db_column='Sawai Madhopur', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jangaon = models.FloatField(db_column='Jangaon', blank=True, null=True)  # Field name made lowercase.
    mancherial = models.FloatField(db_column='Mancherial', blank=True, null=True)  # Field name made lowercase.
    bhadradri = models.FloatField(db_column='Bhadradri', blank=True, null=True)  # Field name made lowercase.
    hydrabad = models.FloatField(db_column='Hydrabad', blank=True, null=True)  # Field name made lowercase.
    karimnagar = models.FloatField(db_column='Karimnagar', blank=True, null=True)  # Field name made lowercase.
    nizamabad = models.FloatField(db_column='Nizamabad', blank=True, null=True)  # Field name made lowercase.
    medak = models.FloatField(db_column='Medak', blank=True, null=True)  # Field name made lowercase.
    rangareddy = models.FloatField(db_column='Rangareddy', blank=True, null=True)  # Field name made lowercase.
    nalgonda = models.FloatField(db_column='Nalgonda', blank=True, null=True)  # Field name made lowercase.
    nagarkurnool = models.FloatField(db_column='Nagarkurnool', blank=True, null=True)  # Field name made lowercase.
    adilabad = models.FloatField(db_column='Adilabad', blank=True, null=True)  # Field name made lowercase.
    komaram_bheem = models.FloatField(db_column='Komaram Bheem', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nirmal = models.FloatField(db_column='Nirmal', blank=True, null=True)  # Field name made lowercase.
    jagtial = models.FloatField(db_column='Jagtial', blank=True, null=True)  # Field name made lowercase.
    kamareddy = models.FloatField(db_column='Kamareddy', blank=True, null=True)  # Field name made lowercase.
    warangal_u = models.FloatField(db_column='Warangal (U)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    jayashankar = models.FloatField(db_column='Jayashankar', blank=True, null=True)  # Field name made lowercase.
    peddapalli = models.FloatField(db_column='Peddapalli', blank=True, null=True)  # Field name made lowercase.
    rajanna_sircilla = models.FloatField(db_column='Rajanna Sircilla', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sangareddy = models.FloatField(db_column='Sangareddy', blank=True, null=True)  # Field name made lowercase.
    siddipet = models.FloatField(db_column='Siddipet', blank=True, null=True)  # Field name made lowercase.
    mahabubabad = models.FloatField(db_column='Mahabubabad', blank=True, null=True)  # Field name made lowercase.
    khammam = models.FloatField(db_column='Khammam', blank=True, null=True)  # Field name made lowercase.
    suryapet = models.FloatField(db_column='Suryapet', blank=True, null=True)  # Field name made lowercase.
    jogulamba = models.FloatField(db_column='Jogulamba', blank=True, null=True)  # Field name made lowercase.
    yadadri = models.FloatField(db_column='Yadadri', blank=True, null=True)  # Field name made lowercase.
    medchal = models.FloatField(db_column='Medchal', blank=True, null=True)  # Field name made lowercase.
    wanaparthy = models.FloatField(db_column='Wanaparthy', blank=True, null=True)  # Field name made lowercase.
    vikarabad = models.FloatField(db_column='Vikarabad', blank=True, null=True)  # Field name made lowercase.
    mahabubnagar = models.FloatField(db_column='Mahabubnagar', blank=True, null=True)  # Field name made lowercase.
    kargil = models.FloatField(db_column='Kargil', blank=True, null=True)  # Field name made lowercase.
    leh_ladakh = models.FloatField(db_column='Leh (Ladakh)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'District_data'
