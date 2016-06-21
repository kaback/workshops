#include <boost/asio.hpp>
#include <boost/asio/posix/stream_descriptor.hpp>
#include <boost/asio/buffer.hpp>
#include <iostream>

// I/O Serviceobjekt
boost::asio::io_service ioservice;

// Stream descriptor STDIN
boost::asio::posix::stream_descriptor in(ioservice, STDIN_FILENO);

// Buffer
std::array<char, 100> bytes;


// Read Handler, wird asynchron aufgerufen, wenn das OS signalisiert,
// dass Daten von STDIN gelesen werden koennen
void read_handler(const boost::system::error_code &ec, std::size_t bytes_transferred)
{
        if (!ec)
        {
                std::cout.write(bytes.data(), bytes_transferred);
                // weiter asynchron von STDIN lesen
                in.async_read_some(boost::asio::buffer(bytes), read_handler);
        }
}


int main()
{
        // asynchron von STDIN lesen
        in.async_read_some(boost::asio::buffer(bytes), read_handler);
        ioservice.run();
}
