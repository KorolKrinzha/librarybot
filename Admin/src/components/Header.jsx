import React from "react";
import { NavLink } from "react-router-dom";
import "../styles/style.css"
import {ReactComponent as HeaderIcon} from '../assets/headericon.svg' 

const Header = () => {
    return (
        <header className="basicheader">
            
        <nav role="navigation">
    
            <a className="nav-brand" href="/">
              <HeaderIcon className="d-inline-block align-center"/>
              librarybot | Админка
            </a>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent">
              <span className="navbar-toggler-icon"></span>
            </button>
    
            <div className="collapse navbar-collapse" id="navbarSupportedContent">
              <ul>
                <li>
                <NavLink to="/logs" className="nav-link text-success">
                    Мой аккаунт
                </NavLink>
    
                </li>
                <li>
                <NavLink to="/create" className="nav-link text-success">
                    Создать новые квизы
                </NavLink>
                </li>
                <li>
                <NavLink to="/users" className="nav-link text-success">
                    Список пользователей
                </NavLink>
                </li>
                <li>
                <NavLink to="/metrics" className="nav-link text-success">
                    Метрики
                </NavLink>
                </li>


              </ul>
    
            </div>
        </nav>
       
        </header>
    );  

}

export default Header;
