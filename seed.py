from flask import Flask
from models import db, Website, Page
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/monitoring_web_itk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    # Optional: clear existing data
    db.session.query(Page).delete()
    db.session.query(Website).delete()
    
    
    # Reset auto-increment counters
    db.session.execute(text("ALTER TABLE pages AUTO_INCREMENT = 1"))
    db.session.execute(text("ALTER TABLE websites AUTO_INCREMENT = 1"))
    
    # Example websites
    websites = [
        Website(nama_web="Prodi Teknik Sipil", link_web="https://ce.itk.ac.id", slug_web="prodi-teknik-sipil"),
        Website(nama_web="Prodi Teknik Kimia", link_web="https://che.itk.ac.id", slug_web="prodi-teknik-kimia"),
        Website(nama_web="Prodi Teknik Elektro", link_web="https://ee.itk.ac.id", slug_web="prodi-teknik-elektro"),
        Website(nama_web="Prodi Teknik Lingkungan", link_web="https://enviro.itk.ac.id", slug_web="prodi-teknik-lingkungan"),
        Website(nama_web="Prodi Teknik Industri", link_web="https://ie.itk.ac.id", slug_web="prodi-teknik-industri"),
        Website(nama_web="Prodi Teknik Informatika", link_web="https://if.itk.ac.id", slug_web="prodi-teknik-informatika"),
        Website(nama_web="Prodi Sistem Informasi", link_web="https://is.itk.ac.id", slug_web="prodi-sistem-informasi"),
        Website(nama_web="Prodi Matematika", link_web="https://math.itk.ac.id", slug_web="prodi-matematika"),
        Website(nama_web="Prodi Teknik Mesin", link_web="https://me.itk.ac.id", slug_web="prodi-teknik-mesin"),
        Website(nama_web="Prodi Teknik Material Metalurgi", link_web="https://mme.itk.ac.id", slug_web="prodi-teknik-material-metalurgi"),
        Website(nama_web="Prodi Teknik Perkapalan", link_web="https://na.itk.ac.id", slug_web="prodi-teknik-perkapalan"),
        Website(nama_web="Prodi Teknik Kelautan", link_web="https://oe.itk.ac.id", slug_web="prodi-teknik-kelautan"),
        Website(nama_web="Prodi Fisika", link_web="https://phy.itk.ac.id", slug_web="prodi-fisika"),
        Website(nama_web="Prodi Perencanaan Wilayah dan Kota", link_web="https://urp.itk.ac.id", slug_web="prodi-perencanaan-wilayah-dan-kota"),
        Website(nama_web="Prodi Arsitektur", link_web="https://ars.itk.ac.id", slug_web="prodi-arsitektur"),
        Website(nama_web="Prodi Statistika", link_web="https://stat.itk.ac.id", slug_web="prodi-statistika"),
        Website(nama_web="Prodi Ilmu Aktuaria", link_web="https://actsci.itk.ac.id", slug_web="prodi-ilmu-aktuaria"),
        Website(nama_web="Prodi Teknik Pangan", link_web="https://foodtech.itk.ac.id", slug_web="prodi-teknik-pangan"),
        Website(nama_web="Prodi Rekayasa Keselamatan", link_web="https://safetyeng.itk.ac.id", slug_web="prodi-rekayasa-keselamatan"),
        Website(nama_web="Prodi Bisnis Digital", link_web="https://bisnisdigital.itk.ac.id", slug_web="prodi-bisnis-digital"),
        Website(nama_web="Prodi Desain Komunikasi Visual", link_web="https://dkv.itk.ac.id", slug_web="prodi-desain-komunikasi-visual"),
        Website(nama_web="Repository", link_web="https://repository.itk.ac.id", slug_web="Repository"),
        Website(nama_web="Perpustakaan", link_web="https://perpustakaan.itk.ac.id", slug_web="Perpustakaan"),
        Website(nama_web="Learning Management Systems", link_web="https://kuliah.itk.ac.id", slug_web="learning-management-systems"),
        Website(nama_web="Dokumen Mutu", link_web="https://dokumen-mutu.itk.ac.id", slug_web="dokumen-mutu"),
        Website(nama_web="Penerimaan Mahasiswa Baru", link_web="https://pmb.itk.ac.id", slug_web="penerimaan-mahasiswa-baru"),
        Website(nama_web="SIM Manajemen", link_web="https://simmanajemen.itk.ac.id", slug_web="sim-manajemen"),
        Website(nama_web="SIPEKA", link_web="https://sipeka.itk.ac.id", slug_web="sipeka"),
        Website(nama_web="SPEAK", link_web="https://speak.itk.ac.id", slug_web="speak"),
        Website(nama_web="SUMMIT", link_web="https://summit.itk.ac.id", slug_web="summit"),
        Website(nama_web="SIMPAS", link_web="https://simpas.itk.ac.id", slug_web="simpas"),
        Website(nama_web="JAMU", link_web="https://jamu.itk.ac.id", slug_web="jamu"),
        Website(nama_web="Short Link ITK", link_web="https://s.itk.ac.id", slug_web="short-link-itk"),
        Website(nama_web="SIRAMA", link_web="https://sirama.itk.ac.id", slug_web="sirama"),
        Website(nama_web="SIM Banding", link_web="https://simbanding.itk.ac.id", slug_web="sim-banding"),
        Website(nama_web="Gerbang", link_web="https://gerbang.itk.ac.id", slug_web="gerbang"),
        Website(nama_web="Host to Host BNI", link_web="https://h2hbni.itk.ac.id", slug_web="host-to-host-bni"),
        Website(nama_web="Host to Host BRI", link_web="https://h2hbri.itk.ac.id", slug_web="host-to-host-bri"),
        Website(nama_web="Host to Host Mandiri", link_web="https://h2hmandiri.itk.ac.id", slug_web="host-to-host-mandiri"),
        Website(nama_web="Tracer Study", link_web="https://tracer.itk.ac.id", slug_web="tracer-study"),
        Website(nama_web="Feeder Gerbang", link_web="https://feeder-gerbang.itk.ac.id", slug_web="feeder-gerbang"),
        Website(nama_web="PPID", link_web="https://ppid.itk.ac.id", slug_web="ppid"),
        Website(nama_web="DPM ITK", link_web="https://dpm.itk.ac.id", slug_web="dpm-itk"),
        Website(nama_web="Open House ITK", link_web="https://openhouse.itk.ac.id", slug_web="open-house-itk"),
        Website(nama_web="Kerjasama ITK", link_web="https://kerjasama.itk.ac.id", slug_web="kerjasama-itk"),
        Website(nama_web="Pilrek ITK", link_web="https://pilrek.itk.ac.id", slug_web="pilrek-itk"),
        Website(nama_web="Unit Layanan Terpadu", link_web="https://ult.itk.ac.id", slug_web="unit-layanan-terpadu"),
        Website(nama_web="Web Profil ITK", link_web="https://itk.ac.id", slug_web="web-profil-itk"),
        Website(nama_web="SPI", link_web="https://spi.itk.ac.id", slug_web="spi"),
        Website(nama_web="UPA TIK", link_web="https://ict.itk.ac.id", slug_web="upa-tik"),
        Website(nama_web="UPA Bahasa", link_web="https://lch.itk.ac.id", slug_web="UPA Bahasa"),
        Website(nama_web="LPPM", link_web="https://lppm.itk.ac.id", slug_web="lppm"),
        Website(nama_web="Dev SCA", link_web="https://dev-sca.itk.ac.id", slug_web="dev-sca"),
        Website(nama_web="Journal", link_web="https://journal.itk.ac.id", slug_web="journal"),
        Website(nama_web="IAET", link_web="https://iaet.itk.ac.id", slug_web="iaet"),
        Website(nama_web="SNBP", link_web="https://snbp.itk.ac.id", slug_web="snbp"),
        Website(nama_web="Inkubator Bisnis", link_web="https://ibt.itk.ac.id", slug_web="inkubator-bisnis"),
        Website(nama_web="CCTV", link_web="https://nvr.itk.ac.id", slug_web="cctv"),
               
        
    ]
   
    
    # Add all websites at once
    db.session.add_all(websites)
    db.session.flush()  # ensure IDs are populated

    # Define pages using the actual website instances
    pages = [
        Page(id_web=websites[0].id_web, halaman_web="/"),
        Page(id_web=websites[0].id_web, halaman_web="/berita"),
        Page(id_web=websites[0].id_web, halaman_web="/profile"),
        Page(id_web=websites[0].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[0].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[0].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[0].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[0].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[0].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[0].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[0].id_web, halaman_web="/login"),
        
        Page(id_web=websites[1].id_web, halaman_web="/"),
        Page(id_web=websites[1].id_web, halaman_web="/berita"),
        Page(id_web=websites[1].id_web, halaman_web="/profile"),
        Page(id_web=websites[1].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[1].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[1].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[1].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[1].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[1].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[1].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[1].id_web, halaman_web="/login"),
        
        Page(id_web=websites[2].id_web, halaman_web="/"),
        Page(id_web=websites[2].id_web, halaman_web="/berita"),
        Page(id_web=websites[2].id_web, halaman_web="/profile"),
        Page(id_web=websites[2].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[2].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[2].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[2].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[2].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[2].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[2].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[2].id_web, halaman_web="/login"),
        
        Page(id_web=websites[3].id_web, halaman_web="/"),
        Page(id_web=websites[3].id_web, halaman_web="/berita"),
        Page(id_web=websites[3].id_web, halaman_web="/profile"),
        Page(id_web=websites[3].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[3].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[3].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[3].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[3].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[3].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[3].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[3].id_web, halaman_web="/login"),
        
        Page(id_web=websites[4].id_web, halaman_web="/"),
        Page(id_web=websites[4].id_web, halaman_web="/berita"),
        Page(id_web=websites[4].id_web, halaman_web="/profile"),
        Page(id_web=websites[4].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[4].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[4].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[4].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[4].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[4].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[4].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[4].id_web, halaman_web="/login"),
        
        Page(id_web=websites[5].id_web, halaman_web="/"),
        Page(id_web=websites[5].id_web, halaman_web="/berita"),
        Page(id_web=websites[5].id_web, halaman_web="/profile"),
        Page(id_web=websites[5].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[5].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[5].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[5].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[5].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[5].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[5].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[5].id_web, halaman_web="/login"),
        
        Page(id_web=websites[6].id_web, halaman_web="/"),
        Page(id_web=websites[6].id_web, halaman_web="/berita"),
        Page(id_web=websites[6].id_web, halaman_web="/profile"),
        Page(id_web=websites[6].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[6].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[6].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[6].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[6].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[6].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[6].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[6].id_web, halaman_web="/login"),
        
        Page(id_web=websites[7].id_web, halaman_web="/"),
        Page(id_web=websites[7].id_web, halaman_web="/berita"),
        Page(id_web=websites[7].id_web, halaman_web="/profile"),
        Page(id_web=websites[7].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[7].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[7].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[7].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[7].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[7].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[7].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[7].id_web, halaman_web="/login"),
        
        Page(id_web=websites[8].id_web, halaman_web="/"),
        Page(id_web=websites[8].id_web, halaman_web="/berita"),
        Page(id_web=websites[8].id_web, halaman_web="/profile"),
        Page(id_web=websites[8].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[8].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[8].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[8].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[8].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[8].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[8].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[8].id_web, halaman_web="/login"),
        
        Page(id_web=websites[9].id_web, halaman_web="/"),
        Page(id_web=websites[9].id_web, halaman_web="/berita"),
        Page(id_web=websites[9].id_web, halaman_web="/profile"),
        Page(id_web=websites[9].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[9].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[9].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[9].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[9].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[9].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[9].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[9].id_web, halaman_web="/login"),
        
        Page(id_web=websites[10].id_web, halaman_web="/"),
        Page(id_web=websites[10].id_web, halaman_web="/berita"),
        Page(id_web=websites[10].id_web, halaman_web="/profile"),
        Page(id_web=websites[10].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[10].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[10].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[10].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[10].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[10].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[10].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[10].id_web, halaman_web="/login"),
        
        Page(id_web=websites[11].id_web, halaman_web="/"),
        Page(id_web=websites[11].id_web, halaman_web="/berita"),
        Page(id_web=websites[11].id_web, halaman_web="/profile"),
        Page(id_web=websites[11].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[11].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[11].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[11].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[11].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[11].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[11].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[11].id_web, halaman_web="/login"),
        
        Page(id_web=websites[12].id_web, halaman_web="/"),
        Page(id_web=websites[12].id_web, halaman_web="/berita"),
        Page(id_web=websites[12].id_web, halaman_web="/profile"),
        Page(id_web=websites[12].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[12].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[12].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[12].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[12].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[12].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[12].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[12].id_web, halaman_web="/login"),
        
        Page(id_web=websites[13].id_web, halaman_web="/"),
        Page(id_web=websites[13].id_web, halaman_web="/berita"),
        Page(id_web=websites[13].id_web, halaman_web="/profile"),
        Page(id_web=websites[13].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[13].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[13].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[13].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[13].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[13].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[13].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[13].id_web, halaman_web="/login"),
        
        Page(id_web=websites[14].id_web, halaman_web="/"),
        Page(id_web=websites[14].id_web, halaman_web="/berita"),
        Page(id_web=websites[14].id_web, halaman_web="/profile"),
        Page(id_web=websites[14].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[14].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[14].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[14].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[14].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[14].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[14].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[14].id_web, halaman_web="/login"),
        
        Page(id_web=websites[15].id_web, halaman_web="/"),
        Page(id_web=websites[15].id_web, halaman_web="/berita"),
        Page(id_web=websites[15].id_web, halaman_web="/profile"),
        Page(id_web=websites[15].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[15].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[15].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[15].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[15].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[15].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[15].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[15].id_web, halaman_web="/login"),
        
        Page(id_web=websites[16].id_web, halaman_web="/"),
        Page(id_web=websites[16].id_web, halaman_web="/berita"),
        Page(id_web=websites[16].id_web, halaman_web="/profile"),
        Page(id_web=websites[16].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[16].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[16].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[16].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[16].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[16].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[16].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[16].id_web, halaman_web="/login"),
        
        Page(id_web=websites[17].id_web, halaman_web="/"),
        Page(id_web=websites[17].id_web, halaman_web="/berita"),
        Page(id_web=websites[17].id_web, halaman_web="/profile"),
        Page(id_web=websites[17].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[17].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[17].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[17].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[17].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[17].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[17].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[17].id_web, halaman_web="/login"),
        
        Page(id_web=websites[18].id_web, halaman_web="/"),
        Page(id_web=websites[18].id_web, halaman_web="/berita"),
        Page(id_web=websites[18].id_web, halaman_web="/profile"),
        Page(id_web=websites[18].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[18].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[18].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[18].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[18].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[18].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[18].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[18].id_web, halaman_web="/login"),
        
        Page(id_web=websites[19].id_web, halaman_web="/"),
        Page(id_web=websites[19].id_web, halaman_web="/berita"),
        Page(id_web=websites[19].id_web, halaman_web="/profile"),
        Page(id_web=websites[19].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[19].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[19].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[19].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[19].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[19].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[19].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[19].id_web, halaman_web="/login"),
        
        Page(id_web=websites[20].id_web, halaman_web="/"),
        Page(id_web=websites[20].id_web, halaman_web="/berita"),
        Page(id_web=websites[20].id_web, halaman_web="/profile"),
        Page(id_web=websites[20].id_web, halaman_web="/profile/sejarah"),
        Page(id_web=websites[20].id_web, halaman_web="/profile/visimisi"),
        Page(id_web=websites[20].id_web, halaman_web="/akademik/kurikulum"),
        Page(id_web=websites[20].id_web, halaman_web="/akademik/silabus"),
        Page(id_web=websites[20].id_web, halaman_web="/kemahasiswaan/ormawa"),
        Page(id_web=websites[20].id_web, halaman_web="/penelitian/grup_penelitian"),
        Page(id_web=websites[20].id_web, halaman_web="/penelitian/kontak"),
        Page(id_web=websites[20].id_web, halaman_web="/login"),
        
        Page(id_web=websites[21].id_web, halaman_web="/"),
        Page(id_web=websites[22].id_web, halaman_web="/"),
        Page(id_web=websites[23].id_web, halaman_web="/"),
        Page(id_web=websites[24].id_web, halaman_web="/"),
        Page(id_web=websites[25].id_web, halaman_web="/"),
        Page(id_web=websites[26].id_web, halaman_web="/"),
        Page(id_web=websites[27].id_web, halaman_web="/"),
        Page(id_web=websites[28].id_web, halaman_web="/"),
        Page(id_web=websites[29].id_web, halaman_web="/"),
        Page(id_web=websites[30].id_web, halaman_web="/"),
        Page(id_web=websites[31].id_web, halaman_web="/"),
        Page(id_web=websites[32].id_web, halaman_web="/"),
        Page(id_web=websites[33].id_web, halaman_web="/"),
        Page(id_web=websites[34].id_web, halaman_web="/"),
        Page(id_web=websites[35].id_web, halaman_web="/"),
        Page(id_web=websites[36].id_web, halaman_web="/"),
        Page(id_web=websites[37].id_web, halaman_web="/"),
        Page(id_web=websites[38].id_web, halaman_web="/"),
        Page(id_web=websites[39].id_web, halaman_web="/"),
        Page(id_web=websites[40].id_web, halaman_web="/"),
        Page(id_web=websites[41].id_web, halaman_web="/"),
        Page(id_web=websites[42].id_web, halaman_web="/"),
        Page(id_web=websites[43].id_web, halaman_web="/"),
        Page(id_web=websites[44].id_web, halaman_web="/"),
        Page(id_web=websites[45].id_web, halaman_web="/"),
        Page(id_web=websites[46].id_web, halaman_web="/"),
        Page(id_web=websites[47].id_web, halaman_web="/"),
        Page(id_web=websites[48].id_web, halaman_web="/"),
        Page(id_web=websites[49].id_web, halaman_web="/"),
        Page(id_web=websites[50].id_web, halaman_web="/"),
        Page(id_web=websites[51].id_web, halaman_web="/"),
        Page(id_web=websites[52].id_web, halaman_web="/"),
        Page(id_web=websites[53].id_web, halaman_web="/"),
        Page(id_web=websites[54].id_web, halaman_web="/"),
        Page(id_web=websites[55].id_web, halaman_web="/"),
        Page(id_web=websites[56].id_web, halaman_web="/"),
        Page(id_web=websites[57].id_web, halaman_web="/"),
       
    ]

    db.session.add_all(pages)
    db.session.commit()

    print("✅ Database seeded successfully.")


