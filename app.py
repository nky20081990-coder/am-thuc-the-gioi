import streamlit as st
import html
import urllib.parse

# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Ẩm Thực Thế Giới",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS - GIAO DIỆN
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Be Vietnam Pro', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(255,190,92,.16), transparent 30%),
        radial-gradient(circle at top right, rgba(255,99,71,.12), transparent 25%),
        #fffaf3;
}

/* Header */

.hero {
    padding: 45px 35px;
    border-radius: 28px;
    background:
        linear-gradient(135deg, #7f1d1d, #dc2626 55%, #f59e0b);
    color: white;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0 15px 45px rgba(127,29,29,.25);
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    opacity: .92;
}

/* Section */

.section-title {
    font-size: 30px;
    font-weight: 800;
    color: #7f1d1d;
    margin-top: 15px;
    margin-bottom: 20px;
}

/* Cards */

.food-card {
    background: white;
    border-radius: 20px;
    padding: 22px;
    margin-bottom: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,.07);
    border: 1px solid rgba(127,29,29,.08);
    transition: .25s;
}

.food-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 15px 35px rgba(0,0,0,.12);
}

.food-card h3 {
    color: #991b1b;
    margin-bottom: 8px;
}

.country-card {
    background: white;
    border-radius: 18px;
    padding: 25px;
    min-height: 150px;
    box-shadow: 0 8px 25px rgba(0,0,0,.07);
    border: 1px solid #f1e5d5;
}

.country-card h3 {
    color: #7f1d1d;
}

/* Recipe */

.recipe-title {
    font-size: 40px;
    font-weight: 800;
    color: #7f1d1d;
}

.recipe-box {
    background: white;
    border-radius: 22px;
    padding: 28px;
    margin: 20px 0;
    box-shadow: 0 8px 30px rgba(0,0,0,.08);
}

.ingredient {
    padding: 8px 0;
    border-bottom: 1px solid #eee;
}

.step {
    background: #fff7ed;
    padding: 15px 18px;
    margin: 12px 0;
    border-left: 5px solid #ea580c;
    border-radius: 8px;
}

/* Footer */

.footer {
    text-align: center;
    padding: 40px 10px;
    margin-top: 50px;
    color: #777;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# DỮ LIỆU MÓN ĂN
# =========================================================

FOODS = {

# =========================================================
# CHÂU Á
# =========================================================

"Châu Á": {

"Việt Nam": {

"Phở": {
"emoji": "🍜",
"intro": "Phở là món ăn biểu tượng của Việt Nam, nổi tiếng với nước dùng trong, thơm và đậm đà cùng bánh phở mềm.",
"ingredients": [
"Bánh phở",
"Thịt bò hoặc thịt gà",
"Xương bò",
"Hành tây",
"Gừng",
"Quế, hồi",
"Nước mắm",
"Muối, đường, tiêu",
"Rau thơm, chanh, ớt"
],
"steps": [
"Nướng sơ hành tây và gừng để tạo mùi thơm.",
"Ninh xương bò với nước trong nhiều giờ, thường xuyên vớt bọt.",
"Cho quế, hồi và các gia vị vào nồi nước dùng.",
"Nêm nước mắm, muối và đường cho vừa khẩu vị.",
"Trụng bánh phở rồi cho vào tô.",
"Xếp thịt lên trên, chan nước dùng nóng.",
"Ăn kèm rau thơm, chanh và ớt."
]
},

"Bánh mì": {
"emoji": "🥖",
"intro": "Bánh mì Việt Nam là sự kết hợp giữa bánh mì giòn, thịt, đồ chua, rau thơm và nước sốt.",
"ingredients": [
"Bánh mì",
"Thịt nguội hoặc thịt nướng",
"Pate",
"Dưa leo",
"Rau mùi",
"Cà rốt và củ cải ngâm",
"Nước sốt"
],
"steps": [
"Cắt bánh mì theo chiều dọc.",
"Phết pate và nước sốt vào bên trong.",
"Cho thịt nguội hoặc thịt nướng vào.",
"Thêm dưa leo, rau mùi và đồ chua.",
"Thưởng thức ngay khi bánh còn giòn."
]
},

"Bún chả": {
"emoji": "🍢",
"intro": "Bún chả là đặc sản Hà Nội gồm thịt viên, thịt ba chỉ nướng, bún và nước chấm chua ngọt.",
"ingredients": [
"Thịt ba chỉ",
"Thịt heo xay",
"Bún",
"Nước mắm",
"Đường",
"Giấm",
"Tỏi, ớt",
"Cà rốt, đu đủ xanh",
"Rau sống"
],
"steps": [
"Ướp thịt với nước mắm, đường, tiêu và hành tỏi.",
"Vo thịt xay thành từng viên.",
"Nướng thịt viên và thịt ba chỉ đến khi vàng thơm.",
"Pha nước chấm với nước mắm, đường, giấm, tỏi và ớt.",
"Cho cà rốt, đu đủ xanh vào nước chấm.",
"Dùng thịt nướng với bún, rau sống và nước chấm."
]
},

"Gỏi cuốn": {
"emoji": "🥬",
"intro": "Gỏi cuốn là món ăn thanh nhẹ với bánh tráng, rau sống, bún và tôm hoặc thịt.",
"ingredients": [
"Bánh tráng",
"Tôm",
"Thịt heo",
"Bún",
"Xà lách",
"Hẹ",
"Rau thơm",
"Nước chấm"
],
"steps": [
"Luộc tôm và thịt rồi thái mỏng.",
"Nhúng bánh tráng nhanh qua nước.",
"Đặt rau, bún, thịt và tôm lên bánh tráng.",
"Gấp hai mép rồi cuộn chặt tay.",
"Dùng với nước chấm đậu phộng hoặc nước mắm."
]
},

"Cơm tấm": {
"emoji": "🍚",
"intro": "Cơm tấm là món ăn đặc trưng của miền Nam Việt Nam, thường dùng với sườn nướng, bì, chả và nước mắm.",
"ingredients": [
"Gạo tấm",
"Sườn heo",
"Nước mắm",
"Đường",
"Mật ong",
"Tỏi",
"Đồ chua",
"Dưa leo",
"Hành lá"
],
"steps": [
"Nấu gạo tấm thành cơm.",
"Ướp sườn với nước mắm, đường, mật ong và tỏi.",
"Nướng sườn đến khi vàng thơm.",
"Làm mỡ hành và pha nước mắm chua ngọt.",
"Cho cơm ra đĩa, đặt sườn lên trên.",
"Dùng cùng đồ chua, dưa leo và nước mắm."
]
}

},

"Nhật Bản": {

"Sushi": {
"emoji": "🍣",
"intro": "Sushi là món ăn nổi tiếng của Nhật Bản với cơm trộn giấm kết hợp hải sản, rong biển hoặc rau củ.",
"ingredients": [
"Gạo sushi",
"Giấm gạo",
"Đường",
"Muối",
"Cá hồi hoặc cá ngừ",
"Rong biển",
"Dưa leo"
],
"steps": [
"Nấu cơm sushi.",
"Trộn cơm với giấm, đường và muối.",
"Để cơm nguội.",
"Đặt rong biển lên mành cuốn.",
"Trải cơm và nhân lên rong biển.",
"Cuộn chặt rồi cắt thành khoanh."
]
},

"Ramen": {
"emoji": "🍜",
"intro": "Ramen là mì Nhật Bản ăn cùng nước dùng đậm đà, thịt, trứng và các loại rau.",
"ingredients": [
"Mì ramen",
"Nước dùng",
"Thịt heo",
"Trứng",
"Hành lá",
"Rong biển",
"Nước tương"
],
"steps": [
"Nấu nước dùng với thịt và gia vị.",
"Luộc mì ramen.",
"Luộc trứng và cắt đôi.",
"Cho mì vào tô.",
"Chan nước dùng nóng.",
"Thêm thịt, trứng, rong biển và hành."
]
},

"Tempura": {
"emoji": "🍤",
"intro": "Tempura là món chiên kiểu Nhật với lớp bột mỏng, nhẹ và giòn.",
"ingredients": [
"Tôm",
"Rau củ",
"Bột mì",
"Trứng",
"Nước lạnh",
"Dầu ăn"
],
"steps": [
"Sơ chế tôm và rau củ.",
"Pha bột với trứng và nước lạnh.",
"Nhúng nguyên liệu vào bột.",
"Chiên nhanh trong dầu nóng.",
"Vớt ra để ráo dầu.",
"Dùng nóng với nước chấm."
]
}

},

"Hàn Quốc": {

"Bibimbap": {
"emoji": "🍚",
"intro": "Bibimbap là cơm trộn Hàn Quốc gồm cơm, rau củ, thịt, trứng và tương ớt gochujang.",
"ingredients": [
"Cơm trắng",
"Thịt bò",
"Cà rốt",
"Giá đỗ",
"Rau bina",
"Trứng",
"Gochujang",
"Dầu mè"
],
"steps": [
"Xào riêng từng loại rau củ.",
"Ướp và xào thịt bò.",
"Cho cơm vào tô.",
"Sắp rau và thịt thành từng phần.",
"Đặt trứng lên trên.",
"Thêm gochujang và dầu mè.",
"Trộn đều trước khi ăn."
]
},

"Kimchi": {
"emoji": "🥬",
"intro": "Kimchi là món rau củ lên men nổi tiếng của Hàn Quốc, đặc biệt phổ biến với cải thảo.",
"ingredients": [
"Cải thảo",
"Muối",
"Bột ớt Hàn Quốc",
"Tỏi",
"Gừng",
"Nước mắm",
"Đường",
"Hành lá"
],
"steps": [
"Rửa và cắt cải thảo.",
"Ướp cải với muối rồi để cho mềm.",
"Trộn bột ớt với tỏi, gừng và gia vị.",
"Trộn hỗn hợp gia vị với cải thảo.",
"Cho vào hộp sạch.",
"Để lên men ở nhiệt độ phù hợp rồi bảo quản lạnh."
]
},

"Bulgogi": {
"emoji": "🥩",
"intro": "Bulgogi là thịt bò Hàn Quốc thái mỏng, ướp ngọt mặn rồi nướng hoặc áp chảo.",
"ingredients": [
"Thịt bò",
"Nước tương",
"Đường",
"Tỏi",
"Dầu mè",
"Hành tây",
"Hạt mè"
],
"steps": [
"Thái thịt bò thật mỏng.",
"Ướp thịt với nước tương, đường, tỏi và dầu mè.",
"Để thịt thấm gia vị.",
"Áp chảo hoặc nướng trên lửa vừa.",
"Thêm hành tây.",
"Rắc mè trước khi dùng."
]
}

},

"Thái Lan": {

"Pad Thai": {
"emoji": "🍜",
"intro": "Pad Thai là món mì xào nổi tiếng của Thái Lan với vị chua, ngọt, mặn và béo hài hòa.",
"ingredients": [
"Bánh phở khô",
"Tôm",
"Trứng",
"Giá đỗ",
"Đậu phộng",
"Nước me",
"Nước mắm",
"Đường"
],
"steps": [
"Ngâm mềm bánh phở.",
"Pha nước sốt me, nước mắm và đường.",
"Xào tôm.",
"Cho mì và nước sốt vào chảo.",
"Đập trứng và đảo đều.",
"Thêm giá đỗ.",
"Rắc đậu phộng trước khi ăn."
]
},

"Tom Yum": {
"emoji": "🍲",
"intro": "Tom Yum là súp chua cay nổi tiếng của Thái Lan, thường nấu với tôm và các loại thảo mộc.",
"ingredients": [
"Tôm",
"Sả",
"Lá chanh",
"Riềng",
"Nấm",
"Nước cốt chanh",
"Ớt",
"Nước mắm"
],
"steps": [
"Đun nước với sả, riềng và lá chanh.",
"Cho nấm vào nấu.",
"Thêm tôm.",
"Nêm nước mắm và ớt.",
"Tắt bếp rồi cho nước cốt chanh.",
"Dùng nóng."
]
},

"Green Curry": {
"emoji": "🍛",
"intro": "Cà ri xanh Thái có màu xanh đặc trưng từ ớt xanh và các loại thảo mộc.",
"ingredients": [
"Thịt gà",
"Cà ri xanh",
"Nước cốt dừa",
"Cà tím",
"Lá chanh",
"Sả",
"Nước mắm"
],
"steps": [
"Phi thơm sốt cà ri xanh.",
"Cho nước cốt dừa vào.",
"Thêm thịt gà.",
"Cho cà tím và lá chanh.",
"Nêm nước mắm.",
"Nấu đến khi thịt chín."
]
}

},

"Ấn Độ": {

"Biryani": {
"emoji": "🍚",
"intro": "Biryani là cơm gia vị nổi tiếng của Nam Á, thường được nấu cùng thịt và nhiều loại gia vị thơm.",
"ingredients": [
"Gạo basmati",
"Thịt gà",
"Hành tây",
"Sữa chua",
"Quế",
"Bạch đậu khấu",
"Nghệ",
"Thì là"
],
"steps": [
"Ướp thịt với sữa chua và gia vị.",
"Nấu sơ gạo basmati.",
"Xào hành tây.",
"Xếp gạo và thịt thành từng lớp.",
"Đậy kín và nấu lửa nhỏ.",
"Trộn nhẹ trước khi dùng."
]
},

"Butter Chicken": {
"emoji": "🍛",
"intro": "Butter Chicken là món gà sốt cà chua, bơ và gia vị đặc trưng của Ấn Độ.",
"ingredients": [
"Thịt gà",
"Cà chua",
"Bơ",
"Whipping cream",
"Tỏi",
"Gừng",
"Garama masala"
],
"steps": [
"Ướp thịt gà với gia vị.",
"Nướng hoặc áp chảo thịt.",
"Nấu sốt cà chua với bơ.",
"Thêm gừng, tỏi và garam masala.",
"Cho thịt gà vào sốt.",
"Thêm kem và nấu thêm vài phút."
]
},

"Samosa": {
"emoji": "🥟",
"intro": "Samosa là bánh chiên hình tam giác với nhân khoai tây và gia vị.",
"ingredients": [
"Bột mì",
"Khoai tây",
"Đậu Hà Lan",
"Hành",
"Bột cà ri",
"Dầu ăn"
],
"steps": [
"Luộc và nghiền khoai tây.",
"Trộn khoai với đậu và gia vị.",
"Làm vỏ bằng bột mì.",
"Gói nhân thành hình tam giác.",
"Chiên đến khi vàng giòn.",
"Dùng nóng."
]
}

},

"Trung Quốc": {

"Vịt quay Bắc Kinh": {
"emoji": "🦆",
"intro": "Vịt quay Bắc Kinh nổi tiếng với lớp da giòn, thịt mềm và cách thưởng thức cùng bánh tráng mỏng.",
"ingredients": [
"Vịt",
"Mật ong",
"Giấm",
"Ngũ vị hương",
"Hành lá",
"Dưa leo",
"Bánh tráng"
],
"steps": [
"Làm sạch và để vịt thật khô.",
"Phết hỗn hợp mật ong và giấm lên da.",
"Để vịt khô trong thời gian phù hợp.",
"Quay vịt đến khi da vàng giòn.",
"Thái lát mỏng.",
"Dùng với bánh tráng, hành và dưa leo."
]
},

"Dim Sum": {
"emoji": "🥟",
"intro": "Dim Sum là tên gọi chung cho nhiều món ăn nhỏ của Trung Quốc, thường được hấp hoặc chiên.",
"ingredients": [
"Bột mì",
"Tôm",
"Thịt heo",
"Nấm",
"Hành lá",
"Nước tương"
],
"steps": [
"Chuẩn bị phần nhân.",
"Làm vỏ bánh mỏng.",
"Cho nhân vào và tạo hình.",
"Hấp hoặc chiên tùy loại.",
"Dùng cùng nước chấm."
]
},

"Kung Pao Chicken": {
"emoji": "🍗",
"intro": "Kung Pao Chicken là món gà xào cay nổi tiếng của Trung Quốc, thường kết hợp đậu phộng và ớt.",
"ingredients": [
"Thịt gà",
"Đậu phộng",
"Ớt khô",
"Hành",
"Tỏi",
"Nước tương",
"Giấm"
],
"steps": [
"Thái nhỏ thịt gà.",
"Ướp thịt với nước tương.",
"Xào thịt gà.",
"Thêm ớt và tỏi.",
"Cho nước sốt vào.",
"Thêm đậu phộng và đảo nhanh."
]
}

},

},

# =========================================================
# CHÂU ÂU
# =========================================================

"Châu Âu": {

"Italia": {

"Pizza Margherita": {
"emoji": "🍕",
"intro": "Pizza Margherita là biểu tượng của ẩm thực Italia với cà chua, mozzarella và lá húng quế.",
"ingredients": [
"Bột mì",
"Men",
"Cà chua",
"Phô mai mozzarella",
"Húng quế",
"Dầu olive",
"Muối"
],
"steps": [
"Nhào bột với men, nước và muối.",
"Ủ bột cho nở.",
"Cán bột thành hình tròn.",
"Phết sốt cà chua.",
"Thêm mozzarella và húng quế.",
"Nướng ở nhiệt độ cao đến khi bánh chín."
]
},

"Pasta Carbonara": {
"emoji": "🍝",
"intro": "Carbonara là món pasta nổi tiếng của Italia với trứng, phô mai và thịt muối.",
"ingredients": [
"Mì spaghetti",
"Trứng",
"Phô mai Parmesan",
"Thịt xông khói",
"Tiêu đen"
],
"steps": [
"Luộc mì đến độ vừa chín.",
"Chiên thịt xông khói.",
"Trộn trứng với phô mai.",
"Cho mì nóng vào chảo.",
"Tắt bếp rồi trộn với hỗn hợp trứng.",
"Rắc tiêu đen."
]
},

"Lasagna": {
"emoji": "🍝",
"intro": "Lasagna gồm nhiều lớp pasta, sốt thịt và phô mai nướng cùng nhau.",
"ingredients": [
"Lá lasagna",
"Thịt bò xay",
"Cà chua",
"Phô mai",
"Hành tây",
"Tỏi",
"Sốt bechamel"
],
"steps": [
"Xào thịt với hành và tỏi.",
"Thêm sốt cà chua.",
"Xếp một lớp pasta.",
"Thêm sốt thịt và phô mai.",
"Lặp lại nhiều lớp.",
"Nướng đến khi mặt phô mai vàng."
]
}

},

"Pháp": {

"Ratatouille": {
"emoji": "🥘",
"intro": "Ratatouille là món rau củ hầm nổi tiếng của Pháp, có hương vị nhẹ và thơm.",
"ingredients": [
"Cà tím",
"Bí ngòi",
"Cà chua",
"Ớt chuông",
"Hành tây",
"Tỏi",
"Dầu olive"
],
"steps": [
"Cắt rau củ thành miếng vừa ăn.",
"Xào riêng từng loại rau.",
"Cho tất cả vào nồi.",
"Thêm cà chua và gia vị.",
"Hầm lửa nhỏ đến khi rau mềm."
]
},

"Coq au Vin": {
"emoji": "🍗",
"intro": "Coq au Vin là món gà hầm kiểu Pháp với rau củ và nước sốt đậm đà.",
"ingredients": [
"Thịt gà",
"Hành tây",
"Cà rốt",
"Nấm",
"Nước dùng",
"Gia vị"
],
"steps": [
"Áp chảo gà cho vàng.",
"Xào hành, cà rốt và nấm.",
"Cho gà trở lại nồi.",
"Thêm nước dùng.",
"Hầm đến khi thịt mềm."
]
},

"Crêpe": {
"emoji": "🥞",
"intro": "Crêpe là loại bánh mỏng của Pháp, có thể dùng với nhân ngọt hoặc mặn.",
"ingredients": [
"Bột mì",
"Trứng",
"Sữa",
"Đường",
"Bơ"
],
"steps": [
"Trộn bột, trứng và sữa.",
"Để bột nghỉ.",
"Làm nóng chảo.",
"Đổ một lớp bột thật mỏng.",
"Rán hai mặt.",
"Dùng với trái cây hoặc nhân tùy thích."
]
}

},

"Tây Ban Nha": {

"Paella": {
"emoji": "🥘",
"intro": "Paella là món cơm nổi tiếng của Tây Ban Nha, thường nấu cùng hải sản hoặc thịt.",
"ingredients": [
"Gạo",
"Tôm",
"Mực",
"Nghêu",
"Cà chua",
"Nghệ hoặc saffron",
"Hành",
"Tỏi"
],
"steps": [
"Xào hành, tỏi và cà chua.",
"Cho gạo vào đảo.",
"Thêm nước dùng và gia vị.",
"Xếp hải sản lên trên.",
"Nấu đến khi gạo chín và nước cạn."
]
},

"Tortilla Española": {
"emoji": "🥔",
"intro": "Tortilla Española là trứng chiên kiểu Tây Ban Nha với khoai tây và hành tây.",
"ingredients": [
"Khoai tây",
"Trứng",
"Hành tây",
"Dầu olive",
"Muối"
],
"steps": [
"Thái khoai tây mỏng.",
"Chiên mềm khoai và hành.",
"Đánh trứng với muối.",
"Trộn khoai với trứng.",
"Chiên thành bánh tròn.",
"Lật bánh và chiên mặt còn lại."
]
},

"Gazpacho": {
"emoji": "🍅",
"intro": "Gazpacho là súp lạnh của Tây Ban Nha, nổi bật với cà chua và rau củ tươi.",
"ingredients": [
"Cà chua",
"Dưa leo",
"Ớt chuông",
"Hành",
"Tỏi",
"Dầu olive",
"Giấm"
],
"steps": [
"Cắt nhỏ rau củ.",
"Cho tất cả vào máy xay.",
"Thêm dầu olive và giấm.",
"Xay đến khi mịn.",
"Nêm gia vị.",
"Làm lạnh trước khi dùng."
]
}

},

"Hy Lạp": {

"Moussaka": {
"emoji": "🍆",
"intro": "Moussaka là món nướng nhiều lớp với cà tím, thịt băm và sốt kem.",
"ingredients": [
"Cà tím",
"Thịt bò hoặc cừu xay",
"Cà chua",
"Hành",
"Sốt bechamel",
"Phô mai"
],
"steps": [
"Thái và áp chảo cà tím.",
"Xào thịt với hành và cà chua.",
"Xếp cà tím và thịt thành lớp.",
"Phủ sốt bechamel.",
"Rắc phô mai.",
"Nướng đến khi vàng."
]
},

"Greek Salad": {
"emoji": "🥗",
"intro": "Greek Salad là salad Hy Lạp đơn giản với cà chua, dưa leo, olive và phô mai feta.",
"ingredients": [
"Cà chua",
"Dưa leo",
"Olive",
"Hành tím",
"Phô mai feta",
"Dầu olive",
"Muối"
],
"steps": [
"Cắt cà chua và dưa leo.",
"Thêm hành tím và olive.",
"Cho phô mai feta.",
"Rưới dầu olive.",
"Nêm nhẹ rồi trộn."
]
}

},

"Đức": {

"Bratwurst": {
"emoji": "🌭",
"intro": "Bratwurst là xúc xích Đức thường được nướng hoặc áp chảo và dùng với bánh mì, mù tạt.",
"ingredients": [
"Xúc xích Đức",
"Bánh mì",
"Mù tạt",
"Hành tây"
],
"steps": [
"Đun nóng chảo.",
"Áp chảo hoặc nướng xúc xích.",
"Đảo đều cho vàng.",
"Cho vào bánh mì.",
"Dùng cùng mù tạt."
]
},

"Sauerbraten": {
"emoji": "🥩",
"intro": "Sauerbraten là món thịt bò Đức được ướp chua nhẹ rồi hầm mềm.",
"ingredients": [
"Thịt bò",
"Giấm",
"Hành",
"Cà rốt",
"Lá nguyệt quế",
"Gia vị"
],
"steps": [
"Ướp thịt với giấm và gia vị.",
"Để thịt thấm.",
"Áp chảo thịt.",
"Thêm rau củ và nước.",
"Hầm đến khi thịt mềm.",
"Cắt lát và dùng với nước sốt."
]
}

},

"Anh": {

"Fish and Chips": {
"emoji": "🐟",
"intro": "Fish and Chips là món cá chiên giòn ăn cùng khoai tây chiên, rất phổ biến tại Anh.",
"ingredients": [
"Cá phi lê",
"Bột mì",
"Bột chiên",
"Khoai tây",
"Muối",
"Dầu ăn"
],
"steps": [
"Cắt khoai tây thành thanh.",
"Chiên khoai đến khi vàng.",
"Lăn cá qua bột.",
"Chiên cá trong dầu nóng.",
"Vớt ra để ráo.",
"Dùng cùng khoai tây."
]
},

"Shepherd's Pie": {
"emoji": "🥧",
"intro": "Shepherd's Pie là món nướng với lớp thịt băm phía dưới và khoai tây nghiền phía trên.",
"ingredients": [
"Thịt cừu xay",
"Khoai tây",
"Cà rốt",
"Đậu Hà Lan",
"Hành tây",
"Bơ",
"Sữa"
],
"steps": [
"Nấu khoai tây rồi nghiền với bơ và sữa.",
"Xào thịt cùng hành và rau củ.",
"Cho thịt vào khuôn.",
"Phủ khoai tây nghiền.",
"Nướng đến khi mặt bánh vàng."
]
}

}

},

# =========================================================
# CHÂU MỸ
# =========================================================

"Châu Mỹ": {

"Mỹ": {

"Hamburger": {
"emoji": "🍔",
"intro": "Hamburger là món ăn phổ biến toàn cầu, gồm bánh mì kẹp nhân thịt cùng rau và nước sốt.",
"ingredients": [
"Bánh burger",
"Thịt bò xay",
"Phô mai",
"Xà lách",
"Cà chua",
"Hành",
"Sốt burger"
],
"steps": [
"Trộn và tạo hình thịt bò.",
"Áp chảo thịt đến độ chín mong muốn.",
"Nướng nhẹ mặt bánh.",
"Đặt thịt lên bánh.",
"Thêm phô mai và rau.",
"Thêm nước sốt rồi kẹp bánh."
]
},

"Apple Pie": {
"emoji": "🥧",
"intro": "Apple Pie là bánh táo nổi tiếng của Mỹ với lớp vỏ nướng giòn và nhân táo quế.",
"ingredients": [
"Táo",
"Bột mì",
"Bơ",
"Đường",
"Bột quế",
"Trứng"
],
"steps": [
"Gọt và thái táo.",
"Trộn táo với đường và quế.",
"Làm phần vỏ bánh.",
"Cho nhân táo vào.",
"Phủ lớp bột phía trên.",
"Quét trứng và nướng đến khi vàng."
]
},

"Mac and Cheese": {
"emoji": "🧀",
"intro": "Mac and Cheese là mì pasta nấu cùng sốt phô mai béo ngậy.",
"ingredients": [
"Mì macaroni",
"Phô mai cheddar",
"Sữa",
"Bơ",
"Bột mì",
"Muối"
],
"steps": [
"Luộc mì.",
"Làm sốt bằng bơ và bột mì.",
"Thêm sữa.",
"Cho phô mai vào khuấy tan.",
"Trộn mì với sốt.",
"Có thể nướng thêm để mặt trên vàng."
]
}

},

"Mexico": {

"Tacos": {
"emoji": "🌮",
"intro": "Tacos là món bánh tortilla kẹp nhân nổi tiếng của Mexico.",
"ingredients": [
"Tortilla",
"Thịt bò hoặc gà",
"Cà chua",
"Hành",
"Rau mùi",
"Chanh",
"Ớt"
],
"steps": [
"Ướp và xào thịt.",
"Làm nóng tortilla.",
"Cho thịt vào bánh.",
"Thêm hành, cà chua và rau mùi.",
"Vắt chanh.",
"Gấp bánh và thưởng thức."
]
},

"Guacamole": {
"emoji": "🥑",
"intro": "Guacamole là sốt bơ nghiền nổi tiếng của Mexico, thường ăn kèm tortilla chips.",
"ingredients": [
"Bơ",
"Cà chua",
"Hành tím",
"Nước cốt chanh",
"Rau mùi",
"Muối"
],
"steps": [
"Bổ đôi quả bơ và lấy phần thịt.",
"Nghiền bơ.",
"Thêm cà chua và hành.",
"Cho nước cốt chanh.",
"Thêm rau mùi và muối.",
"Trộn đều."
]
},

"Enchiladas": {
"emoji": "🌯",
"intro": "Enchiladas là tortilla cuộn nhân, phủ sốt cay và phô mai rồi nướng.",
"ingredients": [
"Tortilla",
"Thịt gà",
"Sốt ớt",
"Phô mai",
"Hành"
],
"steps": [
"Nấu và xé nhỏ thịt gà.",
"Cho thịt vào tortilla.",
"Cuộn lại.",
"Xếp vào khay.",
"Phủ sốt ớt và phô mai.",
"Nướng đến khi phô mai tan."
]
}

},

"Brazil": {

"Feijoada": {
"emoji": "🍲",
"intro": "Feijoada là món hầm đậu đen và thịt rất nổi tiếng của Brazil.",
"ingredients": [
"Đậu đen",
"Thịt heo",
"Xúc xích",
"Hành",
"Tỏi",
"Lá nguyệt quế",
"Muối"
],
"steps": [
"Ngâm đậu.",
"Nấu đậu với thịt.",
"Thêm xúc xích.",
"Phi thơm hành và tỏi.",
"Cho vào nồi hầm.",
"Nấu đến khi đậu và thịt mềm."
]
},

"Pão de Queijo": {
"emoji": "🧀",
"intro": "Pão de Queijo là bánh phô mai nhỏ, bên ngoài hơi giòn và bên trong mềm.",
"ingredients": [
"Bột khoai mì",
"Phô mai",
"Trứng",
"Sữa",
"Dầu",
"Muối"
],
"steps": [
"Đun sữa và dầu.",
"Trộn với bột khoai mì.",
"Thêm trứng và phô mai.",
"Nhào thành hỗn hợp.",
"Vo viên nhỏ.",
"Nướng đến khi bánh phồng vàng."
]
},

"Moqueca": {
"emoji": "🍤",
"intro": "Moqueca là món hải sản hầm nổi tiếng của Brazil với cà chua, hành và nước cốt dừa.",
"ingredients": [
"Tôm hoặc cá",
"Cà chua",
"Hành",
"Ớt chuông",
"Nước cốt dừa",
"Rau mùi"
],
"steps": [
"Ướp hải sản.",
"Xào hành và cà chua.",
"Cho hải sản vào.",
"Thêm nước cốt dừa.",
"Nấu nhẹ đến khi hải sản chín.",
"Rắc rau mùi."
]
}

},

"Peru": {

"Ceviche": {
"emoji": "🐟",
"intro": "Ceviche là món cá sống được xử lý bằng nước cốt chanh, rất nổi tiếng của Peru.",
"ingredients": [
"Cá trắng tươi",
"Nước cốt chanh",
"Hành tím",
"Ớt",
"Rau mùi",
"Muối"
],
"steps": [
"Cắt cá thành miếng nhỏ.",
"Trộn cá với nước cốt chanh.",
"Thêm hành, ớt và rau mùi.",
"Nêm muối.",
"Để cá được xử lý bởi acid trong thời gian ngắn.",
"Dùng ngay khi còn tươi."
]
},

"Lomo Saltado": {
"emoji": "🥩",
"intro": "Lomo Saltado là món bò xào kiểu Peru kết hợp ảnh hưởng ẩm thực Trung Hoa.",
"ingredients": [
"Thịt bò",
"Cà chua",
"Hành tây",
"Nước tương",
"Khoai tây",
"Rau mùi"
],
"steps": [
"Thái thịt bò thành miếng.",
"Chiên khoai tây.",
"Xào nhanh thịt bò trên lửa lớn.",
"Thêm hành và cà chua.",
"Thêm nước tương.",
"Cho khoai tây vào đảo nhanh."
]
}

},

"Argentina": {

"Asado": {
"emoji": "🥩",
"intro": "Asado là phong cách thịt nướng nổi tiếng của Argentina, thường được nướng chậm trên than.",
"ingredients": [
"Thịt bò",
"Muối",
"Tiêu",
"Chimichurri"
],
"steps": [
"Chuẩn bị thịt.",
"Ướp muối vừa phải.",
"Làm nóng than.",
"Nướng thịt từ từ.",
"Lật đều các mặt.",
"Để thịt nghỉ trước khi cắt.",
"Dùng với chimichurri."
]
},

"Empanadas": {
"emoji": "🥟",
"intro": "Empanadas là bánh nhân thịt hoặc rau củ được gói kín rồi nướng hoặc chiên.",
"ingredients": [
"Bột mì",
"Thịt bò xay",
"Hành",
"Trứng",
"Gia vị"
],
"steps": [
"Xào thịt với hành.",
"Làm vỏ bánh.",
"Cho nhân vào giữa.",
"Gấp và ép kín mép.",
"Nướng hoặc chiên đến khi vàng."
]
}

},

"Canada": {

"Poutine": {
"emoji": "🍟",
"intro": "Poutine là món khoai tây chiên phủ phô mai curd và nước sốt gravy, đặc trưng của Canada.",
"ingredients": [
"Khoai tây",
"Phô mai curd",
"Nước sốt gravy",
"Muối"
],
"steps": [
"Cắt khoai tây thành thanh.",
"Chiên khoai đến khi giòn.",
"Cho khoai ra đĩa.",
"Thêm phô mai curd.",
"Rưới nước sốt gravy nóng."
]
},

"Pancakes with Maple Syrup": {
"emoji": "🥞",
"intro": "Bánh pancake dùng với siro cây phong là một món ăn sáng quen thuộc tại Canada.",
"ingredients": [
"Bột mì",
"Trứng",
"Sữa",
"Đường",
"Bột nở",
"Bơ",
"Siro cây phong"
],
"steps": [
"Trộn bột mì, đường và bột nở.",
"Thêm trứng và sữa.",
"Khuấy đến khi vừa hòa quyện.",
"Đổ bột vào chảo nóng.",
"Rán hai mặt.",
"Dùng cùng bơ và siro cây phong."
]
}

}

}

}


# =========================================================
# SESSION STATE
# =========================================================

if "continent" not in st.session_state:
    st.session_state.continent = None

if "country" not in st.session_state:
    st.session_state.country = None

if "food" not in st.session_state:
    st.session_state.food = None


# =========================================================
# HÀM ẢNH
# =========================================================

def get_image_url(food_name):
    query = urllib.parse.quote(
        food_name.replace(" ", "+")
    )

    return f"https://source.unsplash.com/1200x700/?{query},food"


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero">

<h1>🌏 ẨM THỰC THẾ GIỚI</h1>

<p>
Khám phá những món ăn nổi tiếng từ Châu Á, Châu Âu và Châu Mỹ
</p>

<p>
🍜 Văn hóa • 🥘 Hương vị • 👨‍🍳 Cách nấu
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🌏 Bản đồ ẩm thực")

    st.markdown(
        "Khám phá ẩm thực theo từng châu lục và quốc gia."
    )

    st.divider()

    continent_options = [
        "🏠 Trang chủ",
        "🌏 Châu Á",
        "🌍 Châu Âu",
        "🌎 Châu Mỹ"
    ]

    selected = st.radio(
        "Chọn khu vực",
        continent_options
    )

    if selected == "🏠 Trang chủ":
        st.session_state.continent = None
        st.session_state.country = None
        st.session_state.food = None

    else:

        continent = selected.split(" ", 1)[1]

        st.session_state.continent = continent

        countries = list(
            FOODS[continent].keys()
        )

        country = st.selectbox(
            "Chọn quốc gia",
            ["-- Chọn quốc gia --"] + countries
        )

        if country != "-- Chọn quốc gia --":
            st.session_state.country = country

            foods = list(
                FOODS[continent][country].keys()
            )

            food = st.selectbox(
                "Chọn món ăn",
                ["-- Chọn món --"] + foods
            )

            if food != "-- Chọn món --":
                st.session_state.food = food


# =========================================================
# TRANG CHỦ
# =========================================================

if st.session_state.continent is None:

    st.markdown(
        '<div class="section-title">🌐 Khám phá 3 nền ẩm thực lớn</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(3)

    continents = [
        ("🌏", "Châu Á", "Ẩm thực đa dạng với hàng nghìn năm lịch sử."),
        ("🌍", "Châu Âu", "Tinh hoa ẩm thực với nghệ thuật chế biến đặc sắc."),
        ("🌎", "Châu Mỹ", "Sự giao thoa giữa nhiều nền văn hóa và hương vị.")
    ]

    for col, item in zip(cols, continents):

        emoji, name, description = item

        with col:

            st.markdown(
                f"""
                <div class="country-card">

                <div style="font-size:50px">{emoji}</div>

                <h3>{name}</h3>

                <p>{description}</p>

                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"Khám phá {name}",
                key=f"continent_{name}",
                use_container_width=True
            ):

                st.session_state.continent = name

                st.rerun()


    st.markdown("---")

    st.markdown(
        '<div class="section-title">🍽️ Website có gì?</div>',
        unsafe_allow_html=True
    )

    feature_cols = st.columns(4)

    features = [
        ("🌏", "3 châu lục"),
        ("🌎", "18 quốc gia"),
        ("🍜", "50 món ăn"),
        ("👨‍🍳", "Công thức nấu")
    ]

    for col, feature in zip(feature_cols, features):

        with col:

            st.markdown(
                f"""
                <div class="food-card"
                     style="text-align:center">

                    <div style="font-size:40px">
                        {feature[0]}
                    </div>

                    <h3>{feature[1]}</h3>

                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# CHỌN CHÂU LỤC
# =========================================================

elif st.session_state.country is None:

    continent = st.session_state.continent

    icons = {
        "Châu Á": "🌏",
        "Châu Âu": "🌍",
        "Châu Mỹ": "🌎"
    }

    st.markdown(
        f"""
        <div class="section-title">
            {icons[continent]} Ẩm thực {continent}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "Hãy chọn một quốc gia để khám phá những món ăn đặc trưng."
    )

    countries = list(
        FOODS[continent].keys()
    )

    cols = st.columns(3)

    for index, country in enumerate(countries):

        with cols[index % 3]:

            food_count = len(
                FOODS[continent][country]
            )

            st.markdown(
                f"""
                <div class="country-card">

                <h3>🍽️ {country}</h3>

                <p>
                    <b>{food_count}</b> món ăn nổi tiếng
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"Khám phá {country}",
                key=f"country_{continent}_{country}",
                use_container_width=True
            ):

                st.session_state.country = country

                st.rerun()


# =========================================================
# DANH SÁCH MÓN ĂN
# =========================================================

elif st.session_state.food is None:

    continent = st.session_state.continent
    country = st.session_state.country

    st.markdown(
        f"""
        <div class="section-title">
            🍽️ Ẩm thực {country}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        f"Những món ăn tiêu biểu của {country}."
    )

    foods = FOODS[continent][country]

    cols = st.columns(2)

    for index, (food_name, food_data) in enumerate(
        foods.items()
    ):

        with cols[index % 2]:

            st.markdown(
                f"""
                <div class="food-card">

                <div style="font-size:50px">
                    {food_data["emoji"]}
                </div>

                <h3>{food_name}</h3>

                <p>
                    {food_data["intro"]}
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"👨‍🍳 Xem cách nấu {food_name}",
                key=f"food_{continent}_{country}_{food_name}",
                use_container_width=True
            ):

                st.session_state.food = food_name

                st.rerun()


# =========================================================
# CHI TIẾT MÓN ĂN
# =========================================================

else:

    continent = st.session_state.continent
    country = st.session_state.country
    food_name = st.session_state.food

    food = FOODS[continent][country][food_name]

    # Nút quay lại

    if st.button("← Quay lại danh sách món ăn"):

        st.session_state.food = None

        st.rerun()

    st.markdown(
        f"""
        <div style="
            text-align:center;
            margin:20px 0 30px 0;
        ">

        <div style="font-size:80px">
            {food["emoji"]}
        </div>

        <div class="recipe-title">
            {food_name}
        </div>

        <p style="font-size:18px;color:#777">
            🇺🇳 {country} • {continent}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # ẢNH
    # =====================================================

    image_url = get_image_url(food_name)

    try:

        st.image(
            image_url,
            use_container_width=True,
            caption=f"{food_name} – Ẩm thực {country}"
        )

    except:

        st.info(
            "Ảnh minh họa chưa tải được. Bạn có thể thay bằng ảnh riêng."
        )

    # =====================================================
    # GIỚI THIỆU
    # =====================================================

    st.markdown(
        '<div class="section-title">📖 Giới thiệu món ăn</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="recipe-box">

        <p style="font-size:18px;line-height:1.8">
            {food["intro"]}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # NGUYÊN LIỆU
    # =====================================================

    st.markdown(
        '<div class="section-title">🥕 Nguyên liệu</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(2)

    for index, ingredient in enumerate(
        food["ingredients"]
    ):

        with cols[index % 2]:

            st.markdown(
                f"""
                <div class="ingredient">
                    🥄 {ingredient}
                </div>
                """,
                unsafe_allow_html=True
            )

    # =====================================================
    # CÁCH NẤU
    # =====================================================

    st.markdown(
        '<div class="section-title">👨‍🍳 Cách nấu</div>',
        unsafe_allow_html=True
    )

    for index, step in enumerate(
        food["steps"],
        start=1
    ):

        st.markdown(
            f"""
            <div class="step">

                <b>Bước {index}</b>

                <div style="
                    margin-top:6px;
                    line-height:1.6;
                ">
                    {step}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # THÔNG TIN VĂN HÓA
    # =====================================================

    st.markdown(
        '<div class="section-title">🌏 Góc văn hóa</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="recipe-box">

        <p>
        <b>{food_name}</b> không chỉ là một món ăn mà còn
        phản ánh văn hóa, nguyên liệu và phong cách sống
        của người dân <b>{country}</b>.
        </p>

        <p>
        Khi thưởng thức một món ăn truyền thống,
        chúng ta cũng đang khám phá một phần lịch sử
        và bản sắc của quốc gia đó.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        <h3>🌏 Ẩm Thực Thế Giới</h3>

        <p>
        Khám phá thế giới qua những món ăn.
        </p>

        <p>
        🇻🇳 Việt Nam • 🌏 Châu Á • 🌍 Châu Âu • 🌎 Châu Mỹ
        </p>

    </div>
    """,
    unsafe_allow_html=True
)