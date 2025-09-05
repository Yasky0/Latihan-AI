let nama, kelas;

document.getElementById("button_data").onclick = function(){
    nama = document.getElementById("nama_siswa").value;
    kelas = document.getElementById("kelas_siswa").value;
    console.log(`Nama: ${nama}\nKelas: ${kelas}`);
}