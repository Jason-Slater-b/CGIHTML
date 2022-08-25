#!/usr/pkg/bin/bash
echo "Content-type: text/html"
echo ""
cat << 'EOF'
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa"
        crossorigin="anonymous"></script>

    <style>
        @import url('https://fonts.googleapis.com/css?family=Open+Sans');

        html {
            font-family: Arial;
            font-size: 15px;
            background: #5e42a6;
        }

        .sidebar {
            position: fixed;
            width: 25%;
            height: 100vh;
            background: #312450;
            font-size: 0.65em;
        }

        .nav {
            position: relative;
            margin: 0 15%;
            text-align: right;
            top: 50%;
            transform: translateY(-50%);
            font-weight: bold;
        }

        .nav ul {
            list-style: none;
        }

        li {
            position: relative;
            margin: -10px;
        }

        a {
            line-height: 5em;
            text-transform: uppercase;
            text-decoration: none;
            letter-spacing: 0.4em;
            color: rgba(#FFF, 0.35);
            display: block;
            transition: all ease-out 300ms;
        }

        .active a {
            color: white;
        }

        :not(.active)::after {
            opacity: 0.2;
        }

        :not(.active):hover a {
            color: rgba(#FFF, 0.75);
        }

        ::after {
            content: '';
            position: absolute;
            width: 100%;
            height: 0.2em;
            background: black;
            left: 0;
            bottom: 0;
            background-image: linear-gradient(to right, #5e42a6, #b74e91)
        }



        .twitter {
            position: relative;
            width: 75%;
            float: right;
            height: 100vh;
        }

        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
        }

        a {
            position: relative;
        }

        img {
            width: 48px;
            height: 48px;
        }


        #ja {
            text-transform: uppercase;
            font-size: 50px;
            letter-spacing: 0.1em;
            color: black;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
</head>

<body>

    <main class="main">
        <aside class="sidebar">
            <nav class="nav">
                <ul>
                    <li class="nav-item"><a class="nav-link" href="#" data-toggle="modal"
                            data-target="#exampleModalCenter">ifConfig</a></li>

                    <li><a href="#" class="nav-link" href="#" data-toggle="modal" data-target="#neofetch">neofetch</a>
                    </li>

                    <li><a a href="#" class="nav-link" href="#" data-toggle="modal" data-target="#neofetch">dns</a></li>

                    <li><a a a href="#" class="nav-link" href="#" data-toggle="modal" data-target="#w">W</a></li>

                    <li><a a a href="#" class="nav-link" href="#" data-toggle="modal" data-target="#gateway">gateway</a>
                    </li>

                    <li><a a a href="#" class="nav-link" href="#" data-toggle="modal"
                            data-target="#resolv">resolv.conf</a></li>

                    <li><a a a href="#" class="nav-link" href="#" data-toggle="modal" data-target="#df">df -h</a></li>

                    <li><a a a href="#" class="nav-link" href="#" data-toggle="modal"
                            data-target="#hostname">hostname</a></li>

                    <li><a a a href="#" class="nav-link" href="#" data-toggle="modal" data-target="#kernel">Version del
                            kernel</a></li>

                    <li><a a a href="#" class="nav-link" href="#" data-toggle="modal" data-target="#operativo">Version
                            del sistema operativo</a></li>

                    <li><a a a href="#" class="nav-link" href="#" data-toggle="modal" data-target="#nmap">nmap
                            localhost</a></li>

                    <li><a a a href="#" class="nav-link" href="#" data-toggle="modal" data-target="#ps">ps $$</a></li>
                </ul>
            </nav>
        </aside>

        <section class="twitter">
            <div class="container">
                <p id="ja">Jason Slater Barreno D&iacute;az</p>
                <p id="ja">5390-18-3691</p>
            </div>
        </section>

        <!-- Modal 1-->
        <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog"
            aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLongTitle">ifConfig</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
EOF
echo "<pre>$(ifconfig)</pre>"
cat << 'EOF'
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">cerrar</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal 2-->
        <div class="modal fade" id="neofetch" tabindex="-1" role="dialog" aria-labelledby="neofetch" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="neofetch">Neofecht</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
EOF
echo "<pre>$()</pre>"
cat << 'EOF'
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">cerrar</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal 3-->
        <div class="modal fade" id="dns" tabindex="-1" role="dialog" aria-labelledby="dns" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="dns">DNS</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
EOF
echo "<pre>$(cat /etc/resolv.conf)</pre>"
cat << 'EOF'
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">cerrar</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal 4-->
        <div class="modal fade" id="w" tabindex="-1" role="dialog" aria-labelledby="w" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="w">W</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
EOF
echo "<pre>$(w)</pre>"
cat << 'EOF'
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">cerrar</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal 5-->
        <div class="modal fade" id="gateway" tabindex="-1" role="dialog" aria-labelledby="gateway" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="gateway">Gateway</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
EOF
echo "<pre>$(netstat -rn)</pre>"
cat << 'EOF'
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">cerrar</button>
                    </div>
                </div>
            </div>
        </div>


        <!-- Modal 6-->
        <div class="modal fade" id="resolv" tabindex="-1" role="dialog" aria-labelledby="resolv" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="resolv">resolv.conf</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
EOF
echo "<pre>$(cat /etc/resolv.conf)</pre>"
cat << 'EOF'
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">cerrar</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal 7-->
        <div class="modal fade" id="df" tabindex="-1" role="dialog" aria-labelledby="df" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="df">df</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
EOF
echo "<pre>$(df -h)</pre>"
cat << 'EOF'
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">cerrar</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal 8-->
        <div class="modal fade" id="hostname" tabindex="-1" role="dialog" aria-labelledby="hostname" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="hostname">hostname</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
EOF
echo "<pre>$(hostname)</pre>"
cat << 'EOF'
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">cerrar</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal 9-->
        <div class="modal fade" id="kernel" tabindex="-1" role="dialog" aria-labelledby="kernel" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="kernel">Version de kernel</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
EOF
echo "<pre>$(cat /proc/version)</pre>"
cat << 'EOF'
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">cerrar</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal 10-->
        <div class="modal fade" id="operativo" tabindex="-1" role="dialog" aria-labelledby="operativo"
            aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="operativo">Version de sistema operativo</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
EOF
echo "<pre>$(uname -mrs)</pre>"
cat << 'EOF'
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">cerrar</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal 11-->
        <div class="modal fade" id="nmap" tabindex="-1" role="dialog" aria-labelledby="nmap" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="nmap">nmap Localhost</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
EOF
echo "<pre>$()</pre>"
cat << 'EOF'
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">cerrar</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal 12-->
        <div class="modal fade" id="ps" tabindex="-1" role="dialog" aria-labelledby="ps" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="ps">ps $$</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
EOF
echo "<pre>$(ps $$)</pre>"
cat << 'EOF'        
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">cerrar</button>
                    </div>
                </div>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js"
            integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk"
            crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.min.js"
            integrity="sha384-ODmDIVzN+pFdexxHEHFBQH3/9/vQ9uori45z4JjnFsRydbmQbmL5t1tQ0culUzyK"
            crossorigin="anonymous"></script>
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
            integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
            crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
            integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
            crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
            integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
            crossorigin="anonymous"></script>

    </main>
</body>

</html>
EOF