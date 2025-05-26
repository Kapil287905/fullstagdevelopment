import { useState } from "react"
import userData from  "./User"
import SingleUser from "./SingleUser"

const AllUser=()=>{
    const [user,setUsers]=useState([])
    const [showUsers,setShowUsers]=useState(false);

    const addAllUsers=()=>{
        setUsers(userData);
        setShowUsers(true)
    }

    const deleteAllUser=()=>{
        setUsers([])
        setShowUsers(false)
    }

    const deleteUser=(id)=>{
        const updatedUsers= user.filter(u=>u.id!==id)
        setUsers(updatedUsers)
        if(updatedUsers.length===0){
            setShowUsers(false)
        }
        console.log()
    }
    

    return(
        <>
            <div>
                <h1>User Management</h1>
                {!showUsers && (<button onClick={addAllUsers}>Add All User</button>) }
                {showUsers && (
                    <>
                        <button onClick={deleteAllUser}>Delete All User</button>
                        <table>
                            <thead>
                                <tr>
                                    <th>Name</th>
                                    <th>Email</th>
                                    <th>phone</th> 
                                    <th>Address</th>
                                </tr>                    
                            </thead>
                            <tbody>
                                {user.map(u=>(
                                    <SingleUser key={u.id} user={u} deleteUser={deleteUser}/>
                                ))}
                            </tbody>
                        </table>
                    </>
                )}                
            </div>
        </>
    )

}

export default AllUser