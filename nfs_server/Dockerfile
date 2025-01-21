FROM fedora:40

# Install nfs-utils
RUN dnf -y install procps nfs-utils rpcbind && dnf clean all

# Copy entrypoint
COPY run_nfs.sh /usr/local/bin/run_nfs.sh
COPY index.html /tmp/index.html

# Create exports dir
RUN mkdir -p /exports \
    && chmod +x /usr/local/bin/run_nfs.sh \
    && chmod +x /tmp/index.html

# Export NFS Ports
EXPOSE 20048/tcp 2049/tcp 111/tcp
# EXPOSE 111/tcp 111/udp 2049/tcp 2049/udp 20048/tcp 20048/udp

# Expose volume
VOLUME /exports

# Launch entrypoint
ENTRYPOINT ["/usr/local/bin/run_nfs.sh"]

CMD ["/exports", "/"]