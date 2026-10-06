import streamlit as st
import random
import base64
from pathlib import Path

st.set_page_config(
    page_title="Hương Vị Thế Giới",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# DỮ LIỆU ẨM THỰC
# 50 MÓN / 30 QUỐC GIA
# =========================

FOODS = {
    "Châu Á": {
        "🇻🇳 Việt Nam": [
            ("Phở", "🍜", "Phở là món ăn biểu tượng của Việt Nam với bánh phở mềm, nước dùng thơm và thịt bò hoặc gà.",
             ["Bánh phở", "Xương bò", "Thịt bò", "Hành tây", "Gừng", "Quế", "Hoa hồi", "Nước mắm"],
             ["Ninh xương với hành và gừng để tạo nước dùng.", "Thêm quế, hồi và gia vị, đun nhỏ lửa.", "Nêm nước mắm, muối và đường vừa ăn.", "Trụng bánh phở, cho thịt vào tô.", "Chan nước dùng nóng và dùng với rau thơm, chanh, ớt."]),
            ("Bánh mì", "🥖", "Bánh mì Việt Nam kết hợp bánh mì giòn với thịt, pate, rau thơm và đồ chua.",
             ["Bánh mì", "Pate", "Thịt nguội hoặc thịt nướng", "Dưa leo", "Rau mùi", "Cà rốt", "Củ cải", "Nước sốt"],
             ["Chuẩn bị bánh mì và các loại nhân.", "Phết pate và nước sốt.", "Cho thịt, dưa leo và rau mùi vào.", "Thêm cà rốt, củ cải ngâm.", "Dùng ngay khi bánh còn giòn."]),
            ("Bún chả", "🍢", "Đặc sản Hà Nội gồm thịt nướng, bún, rau sống và nước chấm chua ngọt.",
             ["Thịt ba chỉ", "Thịt heo xay", "Bún", "Nước mắm", "Đường", "Giấm", "Tỏi", "Rau sống"],
             ["Ướp thịt với nước mắm, đường, tiêu và hành tỏi.", "Vo thịt xay thành viên.", "Nướng thịt đến khi vàng thơm.", "Pha nước chấm chua ngọt.", "Dùng thịt với bún, rau sống và nước chấm."]),
            ("Gỏi cuốn", "🥬", "Gỏi cuốn là món ăn thanh nhẹ với bánh tráng, tôm, thịt, bún và rau.",
             ["Bánh tráng", "Tôm", "Thịt heo", "Bún", "Xà lách", "Rau thơm", "Hẹ", "Nước chấm"],
             ["Luộc tôm và thịt.", "Nhúng bánh tráng nhanh qua nước.", "Xếp rau, bún, thịt và tôm lên bánh.", "Gấp hai mép rồi cuộn chặt.", "Dùng với nước chấm."]),
            ("Cơm tấm", "🍚", "Cơm tấm thường dùng cùng sườn nướng, đồ chua, mỡ hành và nước mắm.",
             ["Gạo tấm", "Sườn heo", "Nước mắm", "Đường", "Tỏi", "Hành lá", "Dưa leo"],
             ["Nấu gạo tấm.", "Ướp sườn với nước mắm, đường và tỏi.", "Nướng sườn đến khi chín vàng.", "Làm mỡ hành và nước mắm.", "Dùng cơm với sườn, dưa leo và nước mắm."])
        ],
        "🇯🇵 Nhật Bản": [
            ("Sushi", "🍣", "Cơm trộn giấm kết hợp hải sản, rong biển hoặc rau củ.",
             ["Gạo sushi", "Giấm gạo", "Cá hồi", "Rong biển", "Dưa leo", "Đường", "Muối"],
             ["Nấu cơm và trộn với giấm, đường, muối.", "Đặt rong biển lên mành cuốn.", "Trải cơm và nhân.", "Cuộn chặt rồi cắt thành khoanh.", "Dùng cùng nước tương và wasabi."]),
            ("Ramen", "🍜", "Mì Nhật với nước dùng đậm đà, thịt, trứng và rau.",
             ["Mì ramen", "Nước dùng", "Thịt heo", "Trứng", "Hành lá", "Rong biển", "Nước tương"],
             ["Nấu nước dùng.", "Luộc mì.", "Luộc trứng.", "Cho mì vào tô và chan nước dùng.", "Thêm thịt, trứng, rong biển và hành."])
        ],
        "🇰🇷 Hàn Quốc": [
            ("Bibimbap", "🍚", "Cơm trộn Hàn Quốc với rau củ, thịt, trứng và tương ớt.",
             ["Cơm", "Thịt bò", "Cà rốt", "Giá đỗ", "Rau bina", "Trứng", "Gochujang"],
             ["Xào riêng các loại rau.", "Xào thịt bò.", "Cho cơm vào tô.", "Sắp rau và thịt lên trên.", "Đặt trứng, thêm gochujang và trộn đều."]),
            ("Kimchi", "🥬", "Kimchi là rau củ lên men nổi tiếng, đặc biệt là kimchi cải thảo.",
             ["Cải thảo", "Muối", "Bột ớt Hàn Quốc", "Tỏi", "Gừng", "Hành lá", "Nước mắm"],
             ["Ướp cải thảo với muối.", "Trộn bột ớt với tỏi, gừng và gia vị.", "Trộn hỗn hợp với cải.", "Cho vào hộp sạch.", "Lên men ở điều kiện phù hợp rồi bảo quản lạnh."])
        ],
        "🇨🇳 Trung Quốc": [
            ("Vịt quay Bắc Kinh", "🦆", "Món vịt nổi tiếng với lớp da vàng giòn và thịt mềm.",
             ["Vịt", "Mật ong", "Giấm", "Ngũ vị hương", "Hành lá", "Dưa leo", "Bánh tráng"],
             ["Làm sạch và làm khô vịt.", "Phết hỗn hợp mật ong và giấm lên da.", "Để da khô.", "Quay đến khi da vàng giòn.", "Thái lát và dùng với bánh tráng, hành, dưa leo."]),
            ("Dim Sum", "🥟", "Tên gọi chung cho nhiều món nhỏ như há cảo, xíu mại và bánh hấp.",
             ["Bột mì", "Tôm", "Thịt heo", "Nấm", "Hành lá"],
             ["Chuẩn bị nhân.", "Làm vỏ bánh mỏng.", "Cho nhân và tạo hình.", "Hấp chín.", "Dùng với nước chấm."])
        ],
        "🇹🇭 Thái Lan": [
            ("Pad Thai", "🍜", "Mì xào Thái có vị chua, ngọt, mặn và thường dùng tôm.",
             ["Bánh phở khô", "Tôm", "Trứng", "Giá đỗ", "Đậu phộng", "Nước me", "Nước mắm"],
             ["Ngâm mềm bánh phở.", "Pha sốt me, nước mắm và đường.", "Xào tôm.", "Cho mì và sốt vào.", "Thêm trứng, giá và đậu phộng."]),
            ("Tom Yum", "🍲", "Súp chua cay nổi tiếng của Thái Lan với tôm và thảo mộc.",
             ["Tôm", "Sả", "Lá chanh", "Riềng", "Nấm", "Chanh", "Ớt", "Nước mắm"],
             ["Đun sả, riềng và lá chanh.", "Cho nấm vào.", "Thêm tôm.", "Nêm nước mắm và ớt.", "Tắt bếp rồi thêm nước chanh."])
        ],
        "🇮🇳 Ấn Độ": [
            ("Biryani", "🍚", "Cơm basmati thơm gia vị nấu cùng thịt.",
             ["Gạo basmati", "Thịt gà", "Hành", "Sữa chua", "Quế", "Bạch đậu khấu", "Nghệ"],
             ["Ướp thịt với sữa chua và gia vị.", "Nấu sơ gạo.", "Xào hành.", "Xếp gạo và thịt thành lớp.", "Đậy kín và nấu lửa nhỏ."]),
            ("Samosa", "🥟", "Bánh chiên hình tam giác với nhân khoai tây và gia vị.",
             ["Bột mì", "Khoai tây", "Đậu Hà Lan", "Hành", "Bột cà ri", "Dầu"],
             ["Nghiền khoai tây.", "Trộn với đậu và gia vị.", "Làm vỏ bánh.", "Gói thành hình tam giác.", "Chiên vàng giòn."])
        ],
        "🇮🇩 Indonesia": [
            ("Nasi Goreng", "🍳", "Cơm chiên Indonesia đậm vị với trứng, thịt và gia vị.",
             ["Cơm nguội", "Trứng", "Tỏi", "Hành", "Nước tương", "Thịt gà"],
             ["Phi thơm tỏi và hành.", "Xào thịt.", "Cho trứng vào.", "Thêm cơm và nước tương.", "Đảo đều đến khi cơm săn và thơm."]),
            ("Satay", "🍢", "Thịt xiên nướng ăn cùng sốt đậu phộng.",
             ["Thịt gà", "Xiên tre", "Nước tương", "Tỏi", "Đậu phộng", "Đường"],
             ["Cắt thịt nhỏ.", "Ướp thịt với gia vị.", "Xiên thịt.", "Nướng đến khi chín vàng.", "Dùng với sốt đậu phộng."])
        ],
        "🇸🇬 Singapore": [
            ("Hainanese Chicken Rice", "🍗", "Cơm gà Hải Nam là món ăn nổi tiếng của Singapore.",
             ["Gà", "Gạo", "Gừng", "Tỏi", "Hành lá", "Dầu mè"],
             ["Luộc gà với gừng.", "Dùng nước luộc gà nấu cơm.", "Làm sốt gừng và hành.", "Chặt gà.", "Dùng gà với cơm và nước sốt."])
        ],
        "🇵🇭 Philippines": [
            ("Chicken Adobo", "🍗", "Gà hầm với nước tương và giấm, mang vị mặn chua đặc trưng.",
             ["Thịt gà", "Nước tương", "Giấm", "Tỏi", "Lá nguyệt quế", "Tiêu"],
             ["Ướp gà với nước tương và giấm.", "Xào tỏi.", "Cho gà vào áp chảo.", "Thêm nước ướp và lá nguyệt quế.", "Hầm đến khi gà mềm."])
        ],
        "🇹🇷 Thổ Nhĩ Kỳ": [
            ("Kebab", "🥙", "Kebab là nhóm món thịt nướng nổi tiếng của Thổ Nhĩ Kỳ.",
             ["Thịt bò hoặc cừu", "Hành", "Tỏi", "Ớt", "Gia vị", "Bánh mì"],
             ["Ướp thịt với gia vị.", "Xiên hoặc tạo hình thịt.", "Nướng trên lửa.", "Cho vào bánh cùng rau.", "Dùng với sốt."])
        ]
    },

    "Châu Âu": {
        "🇮🇹 Italia": [
            ("Pizza Margherita", "🍕", "Pizza kinh điển với cà chua, mozzarella và húng quế.",
             ["Bột mì", "Men", "Cà chua", "Mozzarella", "Húng quế", "Dầu olive"],
             ["Nhào và ủ bột.", "Cán bột thành hình tròn.", "Phết sốt cà chua.", "Thêm mozzarella và húng quế.", "Nướng ở nhiệt độ cao."]),
            ("Pasta Carbonara", "🍝", "Pasta sốt trứng và phô mai, nổi tiếng của Italia.",
             ["Spaghetti", "Trứng", "Parmesan", "Thịt xông khói", "Tiêu"],
             ["Luộc mì.", "Chiên thịt.", "Trộn trứng với phô mai.", "Cho mì nóng vào chảo rồi tắt bếp.", "Trộn sốt trứng và rắc tiêu."])
        ],
        "🇫🇷 Pháp": [
            ("Ratatouille", "🥘", "Món rau củ hầm thanh nhẹ của Pháp.",
             ["Cà tím", "Bí ngòi", "Cà chua", "Ớt chuông", "Hành", "Tỏi", "Dầu olive"],
             ["Cắt rau củ.", "Xào sơ từng loại.", "Cho vào nồi.", "Thêm cà chua và gia vị.", "Hầm đến khi rau mềm."]),
            ("Crêpe", "🥞", "Bánh mỏng của Pháp, có thể dùng nhân ngọt hoặc mặn.",
             ["Bột mì", "Trứng", "Sữa", "Đường", "Bơ"],
             ["Trộn bột, trứng và sữa.", "Để bột nghỉ.", "Làm nóng chảo.", "Đổ lớp bột thật mỏng.", "Rán hai mặt và dùng với nhân."])
        ],
        "🇪🇸 Tây Ban Nha": [
            ("Paella", "🥘", "Cơm nấu cùng hải sản hoặc thịt, đặc trưng Tây Ban Nha.",
             ["Gạo", "Tôm", "Mực", "Nghêu", "Cà chua", "Saffron", "Hành"],
             ["Xào hành, tỏi và cà chua.", "Cho gạo vào đảo.", "Thêm nước dùng và saffron.", "Xếp hải sản lên.", "Nấu đến khi gạo chín và nước cạn."]),
            ("Gazpacho", "🍅", "Súp lạnh từ cà chua và rau củ tươi.",
             ["Cà chua", "Dưa leo", "Ớt chuông", "Hành", "Tỏi", "Dầu olive", "Giấm"],
             ["Cắt rau.", "Cho vào máy xay.", "Thêm dầu olive và giấm.", "Xay mịn.", "Nêm và làm lạnh trước khi dùng."])
        ],
        "🇬🇷 Hy Lạp": [
            ("Moussaka", "🍆", "Món nướng nhiều lớp với cà tím, thịt băm và sốt kem.",
             ["Cà tím", "Thịt băm", "Cà chua", "Hành", "Bechamel", "Phô mai"],
             ["Áp chảo cà tím.", "Xào thịt với cà chua.", "Xếp cà tím và thịt thành lớp.", "Phủ bechamel.", "Rắc phô mai và nướng vàng."]),
            ("Greek Salad", "🥗", "Salad tươi với cà chua, dưa leo, olive và feta.",
             ["Cà chua", "Dưa leo", "Olive", "Hành tím", "Feta", "Dầu olive"],
             ["Cắt rau.", "Thêm olive và hành.", "Cho feta.", "Rưới dầu olive.", "Trộn nhẹ và dùng."])
        ],
        "🇩🇪 Đức": [
            ("Bratwurst", "🌭", "Xúc xích Đức thường được nướng hoặc áp chảo.",
             ["Xúc xích", "Bánh mì", "Mù tạt", "Hành"],
             ["Làm nóng chảo hoặc bếp nướng.", "Nướng xúc xích đến vàng.", "Làm nóng bánh.", "Cho xúc xích vào bánh.", "Dùng với mù tạt."])
        ],
        "🇬🇧 Anh": [
            ("Fish and Chips", "🐟", "Cá chiên giòn ăn cùng khoai tây chiên.",
             ["Cá phi lê", "Bột mì", "Khoai tây", "Dầu", "Muối"],
             ["Cắt khoai.", "Chiên khoai.", "Lăn cá qua bột.", "Chiên cá vàng giòn.", "Dùng cá với khoai."])
        ],
        "🇵🇹 Bồ Đào Nha": [
            ("Bacalhau", "🐟", "Cá tuyết muối là nguyên liệu biểu tượng trong ẩm thực Bồ Đào Nha.",
             ["Cá tuyết muối", "Khoai tây", "Hành", "Trứng", "Olive"],
             ["Ngâm cá để giảm độ mặn.", "Nấu cá.", "Xào hành và khoai.", "Trộn cá với khoai.", "Thêm trứng và olive."])
        ],
        "🇨🇭 Thụy Sĩ": [
            ("Fondue", "🫕", "Phô mai nóng chảy dùng chấm cùng bánh mì.",
             ["Phô mai", "Rượu vang trắng", "Bánh mì", "Bột bắp"],
             ["Đun nóng rượu.", "Thêm phô mai từng ít một.", "Khuấy đến khi mịn.", "Thêm bột bắp.", "Dùng nóng với bánh mì."])
        ],
        "🇦🇹 Áo": [
            ("Wiener Schnitzel", "🥩", "Thịt bê chiên xù là món kinh điển của Áo.",
             ["Thịt bê", "Bột mì", "Trứng", "Bột chiên xù", "Dầu"],
             ["Dần mỏng thịt.", "Lăn qua bột mì.", "Nhúng trứng.", "Phủ bột chiên xù.", "Chiên vàng hai mặt."])
        ],
        "🇳🇱 Hà Lan": [
            ("Stroopwafel", "🧇", "Bánh waffle mỏng kẹp lớp siro caramel.",
             ["Bột mì", "Bơ", "Đường", "Trứng", "Siro caramel"],
             ["Trộn bột thành khối.", "Chia thành viên.", "Ép mỏng và nướng.", "Phết siro caramel.", "Kẹp hai miếng bánh lại."])
        ]
    },

    "Châu Mỹ": {
        "🇺🇸 Mỹ": [
            ("Hamburger", "🍔", "Bánh mì kẹp thịt bò cùng rau, phô mai và nước sốt.",
             ["Bánh burger", "Thịt bò", "Phô mai", "Xà lách", "Cà chua", "Hành", "Sốt"],
             ["Tạo hình thịt.", "Áp chảo thịt.", "Nướng nhẹ bánh.", "Thêm thịt, phô mai và rau.", "Thêm sốt rồi kẹp bánh."]),
            ("Mac and Cheese", "🧀", "Mì macaroni phủ sốt phô mai béo ngậy, một món ăn gia đình phổ biến tại Mỹ.",
             ["Mì macaroni", "Phô mai cheddar", "Sữa", "Bơ", "Bột mì", "Muối"],
             ["Luộc mì đến vừa chín.", "Đun bơ rồi khuấy với bột mì.", "Thêm sữa và khuấy đến khi sốt sánh.", "Cho phô mai vào khuấy tan.", "Trộn mì với sốt và dùng nóng."]),
            ("Apple Pie", "🥧", "Bánh táo với lớp vỏ nướng và nhân táo quế.",
             ["Táo", "Bột mì", "Bơ", "Đường", "Quế", "Trứng"],
             ["Thái táo.", "Trộn táo với đường và quế.", "Làm vỏ bánh.", "Cho nhân vào.", "Phủ bột và nướng vàng."])
        ],
        "🇲🇽 Mexico": [
            ("Tacos", "🌮", "Tortilla kẹp thịt, rau, hành và các loại sốt.",
             ["Tortilla", "Thịt bò", "Cà chua", "Hành", "Rau mùi", "Chanh", "Ớt"],
             ["Xào thịt với gia vị.", "Làm nóng tortilla.", "Cho thịt vào.", "Thêm rau và hành.", "Vắt chanh và thưởng thức."]),
            ("Guacamole", "🥑", "Sốt bơ nghiền nổi tiếng của Mexico.",
             ["Bơ", "Cà chua", "Hành tím", "Chanh", "Rau mùi", "Muối"],
             ["Nghiền bơ.", "Thêm cà chua và hành.", "Cho nước chanh.", "Thêm rau mùi và muối.", "Trộn đều."])
        ],
        "🇧🇷 Brazil": [
            ("Feijoada", "🍲", "Món hầm đậu đen và thịt nổi tiếng Brazil.",
             ["Đậu đen", "Thịt heo", "Xúc xích", "Hành", "Tỏi", "Lá nguyệt quế"],
             ["Ngâm đậu.", "Nấu đậu với thịt.", "Thêm xúc xích.", "Phi hành tỏi.", "Hầm đến khi mềm."]),
            ("Pão de Queijo", "🧀", "Bánh phô mai nhỏ với vỏ hơi giòn và ruột mềm.",
             ["Bột khoai mì", "Phô mai", "Trứng", "Sữa", "Dầu", "Muối"],
             ["Đun sữa và dầu.", "Trộn với bột.", "Thêm trứng và phô mai.", "Vo viên.", "Nướng đến khi phồng vàng."])
        ],
        "🇦🇷 Argentina": [
            ("Asado", "🥩", "Phong cách thịt nướng Argentina nổi tiếng với cách nướng chậm trên than.",
             ["Thịt bò", "Muối", "Tiêu", "Chimichurri"],
             ["Chuẩn bị thịt.", "Ướp muối vừa phải.", "Làm nóng than.", "Nướng thịt từ từ.", "Để thịt nghỉ rồi dùng với chimichurri."]),
            ("Empanadas", "🥟", "Bánh gói nhân thịt hoặc rau củ, nướng hoặc chiên.",
             ["Bột mì", "Thịt bò xay", "Hành", "Trứng", "Gia vị"],
             ["Xào thịt với hành.", "Làm vỏ.", "Cho nhân vào.", "Gấp và ép kín mép.", "Nướng hoặc chiên vàng."])
        ],
        "🇵🇪 Peru": [
            ("Ceviche", "🐟", "Cá tươi được xử lý bằng nước cốt chanh, kết hợp hành và ớt.",
             ["Cá trắng tươi", "Chanh", "Hành tím", "Ớt", "Rau mùi", "Muối"],
             ["Cắt cá nhỏ.", "Trộn với nước chanh.", "Thêm hành, ớt và rau mùi.", "Nêm muối.", "Dùng ngay khi còn tươi."]),
            ("Lomo Saltado", "🥩", "Bò xào nhanh với hành, cà chua và khoai tây.",
             ["Thịt bò", "Cà chua", "Hành", "Nước tương", "Khoai tây"],
             ["Thái thịt.", "Chiên khoai.", "Xào nhanh thịt trên lửa lớn.", "Thêm hành và cà chua.", "Thêm nước tương và khoai."])
        ],
        "🇨🇦 Canada": [
            ("Poutine", "🍟", "Khoai tây chiên phủ phô mai curd và sốt gravy.",
             ["Khoai tây", "Phô mai curd", "Gravy", "Muối"],
             ["Cắt khoai.", "Chiên giòn.", "Cho phô mai lên khoai.", "Rưới gravy nóng.", "Dùng ngay."])
        ],
        "🇨🇱 Chile": [
            ("Pastel de Choclo", "🌽", "Món nướng với lớp ngô nghiền phủ trên nhân thịt.",
             ["Ngô", "Thịt bò", "Hành", "Trứng", "Olive"],
             ["Xào nhân thịt.", "Nghiền ngô.", "Cho nhân vào khuôn.", "Phủ ngô nghiền.", "Nướng đến khi vàng."])
        ],
        "🇨🇴 Colombia": [
            ("Arepas", "🫓", "Bánh ngô dẹt phổ biến trong ẩm thực Colombia.",
             ["Bột ngô", "Nước", "Muối", "Phô mai"],
             ["Trộn bột với nước và muối.", "Tạo bánh dẹt.", "Áp chảo hai mặt.", "Thêm phô mai nếu muốn.", "Dùng nóng."])
        ],
        "🇨🇺 Cuba": [
            ("Ropa Vieja", "🥩", "Thịt bò hầm xé sợi với cà chua và rau củ.",
             ["Thịt bò", "Cà chua", "Hành", "Ớt chuông", "Tỏi"],
             ["Hầm thịt bò đến mềm.", "Xé thịt thành sợi.", "Xào hành, tỏi và ớt.", "Thêm cà chua.", "Cho thịt vào hầm thêm cho thấm."])
        ],
        "🇯🇲 Jamaica": [
            ("Jerk Chicken", "🍗", "Gà ướp gia vị cay thơm rồi nướng theo phong cách Jamaica.",
             ["Gà", "Ớt", "Gừng", "Tỏi", "Hành", "Gia vị"],
             ["Trộn gia vị thành hỗn hợp ướp.", "Ướp gà.", "Để gà thấm.", "Nướng hoặc áp chảo.", "Dùng nóng cùng rau hoặc cơm."])
        ]
    }
}

# =========================
# HÌNH ẢNH
# =========================

IMAGE_URLS = {
    "Phở": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=1400&q=85",
    "Bánh mì": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=1400&q=85",
    "Sushi": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=1400&q=85",
    "Pizza Margherita": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?auto=format&fit=crop&w=1400&q=85",
    "Hamburger": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=1400&q=85",
    "Tacos": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=1400&q=85",
    "Ramen": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=1400&q=85",
    "Paella": "https://images.unsplash.com/photo-1534080564583-6be75777b70a?auto=format&fit=crop&w=1400&q=85"
}

# =========================
# CSS
# =========================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Be Vietnam Pro', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

button[kind="primary"] {
    background: linear-gradient(90deg,#991b1b,#dc2626);
    color: white;
}

.stApp {
    background:
        radial-gradient(circle at 10% 0%, rgba(245,158,11,.13), transparent 28%),
        radial-gradient(circle at 90% 5%, rgba(220,38,38,.10), transparent 25%),
        #fffaf3;
}

.hero {
    padding: 55px 35px;
    border-radius: 30px;
    text-align: center;
    color: white;
    background: linear-gradient(135deg,#7f1d1d,#dc2626 55%,#f59e0b);
    box-shadow: 0 20px 55px rgba(127,29,29,.22);
    margin-bottom: 35px;
}

.hero h1 {
    font-size: clamp(34px,5vw,58px);
    font-weight: 800;
    margin: 0;
}

.hero p {
    font-size: 18px;
    margin: 10px 0 0;
}

.section {
    color:#7f1d1d;
    font-size:30px;
    font-weight:800;
    margin:28px 0 18px;
}

.card {
    background:#fff;
    border:1px solid #f1e6d8;
    border-radius:22px;
    padding:24px;
    box-shadow:0 8px 28px rgba(0,0,0,.07);
    min-height:155px;
}

.card h3 {
    color:#991b1b;
    margin-bottom:8px;
}

.food-card {
    background:#fff;
    border-radius:24px;
    padding:20px;
    border:1px solid #f1e6d8;
    box-shadow:0 8px 25px rgba(0,0,0,.07);
    min-height:250px;
}

.food-emoji {
    font-size:48px;
}

.recipe {
    background:white;
    border-radius:25px;
    padding:30px;
    box-shadow:0 10px 35px rgba(0,0,0,.08);
    border:1px solid #f1e6d8;
}

.step {
    background:#fff7ed;
    border-left:5px solid #ea580c;
    border-radius:10px;
    padding:15px 18px;
    margin:12px 0;
    line-height:1.7;
}

.ingredient {
    background:#fff;
    border:1px solid #eee2d4;
    padding:12px 15px;
    border-radius:12px;
    margin-bottom:10px;
}

.footer {
    margin-top:55px;
    padding:35px;
    text-align:center;
    color:#777;
}

div.stButton > button {
    border-radius:12px;
    font-weight:700;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION
# =========================

if "continent" not in st.session_state:
    st.session_state.continent = None
if "country" not in st.session_state:
    st.session_state.country = None
if "food" not in st.session_state:
    st.session_state.food = None
if "search" not in st.session_state:
    st.session_state.search = ""

def go_home():
    st.session_state.continent = None
    st.session_state.country = None
    st.session_state.food = None

def go_continent(name):
    st.session_state.continent = name
    st.session_state.country = None
    st.session_state.food = None

def go_country(name):
    st.session_state.country = name
    st.session_state.food = None

def go_food(name):
    st.session_state.food = name

# =========================
# SIDEBAR
# =========================

with st.sidebar:
    st.markdown("## 🌏 HƯƠNG VỊ THẾ GIỚI")
    st.caption("Khám phá văn hóa qua ẩm thực.")

    if st.button("🏠 Trang chủ", use_container_width=True):
        go_home()
        st.rerun()

    st.divider()

    st.markdown("### 🔎 Tìm món ăn")

    search = st.text_input(
        "Tên món",
        placeholder="Ví dụ: Phở, Sushi, Pizza...",
        label_visibility="collapsed"
    )

    if search.strip():
        results = []
        for cont, countries in FOODS.items():
            for country, foods in countries.items():
                for food in foods:
                    if search.lower() in food[0].lower():
                        results.append((cont, country, food[0]))

        if results:
            st.markdown("**Kết quả:**")
            for cont, country, food in results:
                if st.button(f"🍽️ {food}", key=f"search_{cont}_{country}_{food}", use_container_width=True):
                    go_continent(cont)
                    st.session_state.country = country
                    st.session_state.food = food
                    st.rerun()
        else:
            st.info("Không tìm thấy món phù hợp.")

    st.divider()

    if st.button("🎲 Khám phá món ngẫu nhiên", use_container_width=True):
        import random
        all_items = []
        for cont_name, country_map in FOODS.items():
            for country_name, food_list in country_map.items():
                for food_item in food_list:
                    all_items.append((cont_name, country_name, food_item[0]))
        chosen = random.choice(all_items)
        st.session_state.continent = chosen[0]
        st.session_state.country = chosen[1]
        st.session_state.food = chosen[2]
        st.rerun()

    st.markdown("### 🧭 Chọn châu lục")

    for cont, icon in [("Châu Á","🌏"),("Châu Âu","🌍"),("Châu Mỹ","🌎")]:
        if st.button(f"{icon} {cont}", key=f"side_{cont}", use_container_width=True):
            go_continent(cont)
            st.rerun()

# =========================
# HEADER
# =========================

st.markdown("""
<div class="hero">
    <h1>🌏 HƯƠNG VỊ THẾ GIỚI</h1>
    <p>Khám phá món ăn • Văn hóa • Nguyên liệu • Cách nấu</p>
</div>
""", unsafe_allow_html=True)

# =========================
# TRANG CHỦ
# =========================

if st.session_state.continent is None:

    st.markdown('<div class="section">🌐 Khám phá 3 châu lục</div>', unsafe_allow_html=True)

    cols = st.columns(3)

    descriptions = {
        "Châu Á": ("🌏", "Từ phở Việt Nam đến sushi Nhật Bản."),
        "Châu Âu": ("🌍", "Tinh hoa ẩm thực và nghệ thuật chế biến."),
        "Châu Mỹ": ("🌎", "Sự giao thoa của nhiều nền văn hóa.")
    }

    for col, cont in zip(cols, descriptions):
        icon, desc = descriptions[cont]
        with col:
            country_count = len(FOODS[cont])
            food_count = sum(len(x) for x in FOODS[cont].values())

            st.markdown(f"""
            <div class="card">
                <div style="font-size:52px">{icon}</div>
                <h3>{cont}</h3>
                <p>{desc}</p>
                <b>{country_count} quốc gia • {food_count} món</b>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Khám phá {cont}", key=f"home_{cont}", use_container_width=True):
                go_continent(cont)
                st.rerun()

    st.markdown('<div class="section">✨ Website có gì?</div>', unsafe_allow_html=True)

    cols = st.columns(4)
    features = [
        ("🗺️","3 châu lục"),
        ("🌎","30 quốc gia"),
        ("🍽️","50 món ăn"),
        ("👨‍🍳","Cách nấu chi tiết")
    ]

    for col, (icon, text) in zip(cols, features):
        with col:
            st.markdown(f"""
            <div class="card" style="text-align:center;min-height:110px">
                <div style="font-size:35px">{icon}</div>
                <b>{text}</b>
            </div>
            """, unsafe_allow_html=True)

# =========================
# CHỌN CHÂU LỤC
# =========================

elif st.session_state.country is None:

    cont = st.session_state.continent
    icon = {"Châu Á":"🌏","Châu Âu":"🌍","Châu Mỹ":"🌎"}[cont]

    st.markdown(f'<div class="section">{icon} {cont}</div>', unsafe_allow_html=True)
    st.write("Chọn một quốc gia để khám phá ẩm thực.")

    countries = list(FOODS[cont].keys())
    cols = st.columns(3)

    for i, country in enumerate(countries):
        with cols[i % 3]:
            count = len(FOODS[cont][country])
            st.markdown(f"""
            <div class="card">
                <h3>{country}</h3>
                <p>🍽️ {count} món tiêu biểu</p>
                <p>Khám phá hương vị và văn hóa.</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Xem món ăn →", key=f"country_btn_{cont}_{country}", use_container_width=True):
                go_country(country)
                st.rerun()

# =========================
# DANH SÁCH MÓN
# =========================

elif st.session_state.food is None:

    cont = st.session_state.continent
    country = st.session_state.country

    if st.button("← Quay lại châu lục"):
        st.session_state.country = None
        st.rerun()

    st.markdown(f'<div class="section">🍽️ Ẩm thực {country}</div>', unsafe_allow_html=True)

    foods = FOODS[cont][country]
    cols = st.columns(2)

    for i, (name, emoji, intro, ingredients, steps) in enumerate(foods):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="food-card">
                <div class="food-emoji">{emoji}</div>
                <h3>{name}</h3>
                <p>{intro}</p>
                <small>🥕 {len(ingredients)} nguyên liệu • 👨‍🍳 {len(steps)} bước</small>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"📖 Xem công thức {name}", key=f"food_btn_{cont}_{country}_{name}", use_container_width=True):
                go_food(name)
                st.rerun()

# =========================
# CHI TIẾT MÓN
# =========================

else:

    cont = st.session_state.continent
    country = st.session_state.country
    food_name = st.session_state.food

    food = next(x for x in FOODS[cont][country] if x[0] == food_name)
    name, emoji, intro, ingredients, steps = food

    if st.button("← Quay lại danh sách món"):
        st.session_state.food = None
        st.rerun()

    st.markdown(f"""
    <div style="text-align:center;margin:20px 0">
        <div style="font-size:85px">{emoji}</div>
        <h1 style="color:#7f1d1d;font-size:44px">{name}</h1>
        <p style="font-size:18px;color:#777">{country} • {cont}</p>
    </div>
    """, unsafe_allow_html=True)

    # Ảnh
    # Ảnh món ăn: ưu tiên ảnh đã cấu hình; nếu món chưa có ảnh,
    # dùng ảnh tìm theo từ khóa. Nếu mạng ảnh không khả dụng,
    # website vẫn hoạt động và hiển thị thẻ minh họa.
    import urllib.parse

    image_url = IMAGE_URLS.get(name)

    if not image_url:
        query = urllib.parse.quote(name + " - food")
        image_url = f"https://placehold.co/1400x800/png?text={query}"

    try:
        st.image(image_url, use_container_width=True, caption=f"{name} • {country}")
    except Exception:
        st.markdown(f"""
        <div style="
            height:380px;
            border-radius:24px;
            background:linear-gradient(135deg,#7f1d1d,#f59e0b);
            display:flex;
            flex-direction:column;
            align-items:center;
            justify-content:center;
            color:white;
            text-align:center;
            margin-bottom:20px;
        ">
            <div style="font-size:100px">{emoji}</div>
            <h2 style="margin:0">{name}</h2>
            <p>Ảnh minh họa • {country}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section">📖 Giới thiệu món ăn</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="recipe"><p style="font-size:18px;line-height:1.8">{intro}</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="section">🥕 Nguyên liệu</div>', unsafe_allow_html=True)

    cols = st.columns(2)
    for i, item in enumerate(ingredients):
        with cols[i % 2]:
            st.markdown(f'<div class="ingredient">🥄 {item}</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">👨‍🍳 Cách nấu</div>', unsafe_allow_html=True)

    for i, step in enumerate(steps, 1):
        st.markdown(f"""
        <div class="step">
            <b>Bước {i}</b><br>
            {step}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section">🌏 Giá trị văn hóa</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="recipe">
        <p>
        <b>{name}</b> là một đại diện tiêu biểu cho văn hóa ẩm thực
        của <b>{country}</b>. Món ăn không chỉ mang giá trị dinh dưỡng
        mà còn thể hiện nguyên liệu, tập quán và phong cách thưởng thức
        của người dân địa phương.
        </p>
        <p>
        Khi tìm hiểu một món ăn, chúng ta cũng đang tìm hiểu về
        lịch sử và văn hóa của quốc gia đó.
        </p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# FOOTER
# =========================

st.markdown("""
<div class="footer">
    <h3>🌏 HƯƠNG VỊ THẾ GIỚI</h3>
    <p>Khám phá thế giới qua những món ăn.</p>
    <p>🇻🇳 Châu Á • 🌍 Châu Âu • 🌎 Châu Mỹ</p>
</div>
""", unsafe_allow_html=True)
