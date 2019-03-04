$(document).ready(function(){
	var countdown = $("#choosen_countdown").val(); //countdown waktu tersisa
	var point = 0; //skor
	var kesempatan_menjawab = 3; //sisa kesempatan menjawab tiap soal
	$("#countdown").text(countdown); 	
	setInterval(function(){ //menghitung mundur sampai detik ke-0, lalu game berakhir
		countdown--;
		$("#countdown").text(countdown);
		if(countdown == 0) {
			alert("Maaf, waktu anda sudah habis. Point anda : " + point)
			location.replace("")
		}
	}, 1000);

	//mencocokkan kata yang diisi dengan kata yg didatabase berdasarkan id kata
	//yang inputnya hidden di game.html, lalu output benar atau salah dikembalikan
	//secara asynchronous
	$("#button_tebak").click(function(){ 
		var tebakan = $("#input_kata").val()
		var id_kata = $("#id_kata").val()
		var url = '/game/' + $("#selected_difficulty").val()
		kesempatan_menjawab--;
		$.ajax({
			method: "POST",
			url: url,
			data : {
				tebakan : tebakan,
				id_kata : id_kata,
				kesempatan_menjawab : kesempatan_menjawab
			},
			success : function(data) {
				if(data.result) {
					point++;
					alert("Selamat! Anda menjawab dengan benar")	
					kata_berikutnya(data)
					$("#result").empty()
				}
				else {
					if(kesempatan_menjawab > 0) {
						$("#result").text(data.output)
						$("#sisa_kesempatan").text("Kesempatan menjawab tinggal " + kesempatan_menjawab + " kali lagi")
					}
					else {
						alert("Maaf, kesempatan menjawab anda sudah habis. Jawaban yang benar : " + data.jawaban_benar)
						kata_berikutnya(data)
						$("#result").empty()
					}
				}
			}
		});
	});	

	//menampilkan halaman yang berisi kata berikutnya
	function kata_berikutnya(response) {
		$("#point").text("Point anda : " + point)
		$("#permuted_kata").text(response.hasil_permutasi_kata)
		//$("#kata_asli").text(response.kata_asli)
		$("#id_kata").val(response.id_kata)
		$("#input_kata").val("")
		kesempatan_menjawab = 3
		$("#sisa_kesempatan").text("Kesempatan menjawab tinggal " + kesempatan_menjawab + " kali lagi")
	}
});