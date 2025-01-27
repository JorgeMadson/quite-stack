home_view = '''<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página inicial</title>
    <style>
        /* Resetando alguns estilos padrões */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Definindo uma fonte moderna */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f7f6;
            color: #333;
            text-align: center;
            padding: 0 20px;
        }

        h1 {
            color: #5c6bc0;
            font-size: 2.5em;
            margin-top: 50px;
        }

        p {
            font-size: 1.2em;
            margin-top: 20px;
            color: #555;
        }

        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        .button {
            background-color: #5c6bc0;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            font-size: 1.1em;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-top: 30px;
        }

        .button:hover {
            background-color: #3f4a87;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Olá, bem-vindo ao meu app em Flask!</h1>
        <p>Estou feliz por ter você aqui.</p>
        <button class="button" onclick="alert('Bem-vindo!')">Clique aqui!</button>
    </div>
</body>
</html>'''